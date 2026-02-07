import re
from datetime import datetime
import pandas as pd
from datetime import datetime, date
from typing import Optional, Any


#----------------cleaning for date tours table-----------------------
def extract_start_date(date_text):
    original = str(date_text).strip()

    # ISO date anywhere
    iso = re.search(r"\d{4}-\d{2}-\d{2}", original)
    if iso:
        dt = datetime.strptime(iso.group(), "%Y-%m-%d").date()
        return dt.strftime("%d-%m-%Y")

    # 1–19 July 1903
    m1 = re.search(r"(\d+)[–-](\d+)\s+([A-Za-z]+)\s+(\d{4})", original)
    if m1:
        d1, _, month, year = m1.groups()
        dt = datetime.strptime(f"{d1} {month} {year}", "%d %B %Y").date()
        return dt.strftime("%d-%m-%Y")

    # 8 July – 4 August 1907
    m2 = re.search(r"(\d+)\s+([A-Za-z]+)\s+[–-]\s+(\d+)\s+([A-Za-z]+)\s+(\d{4})", original)
    if m2:
        d1, month, _, _, year = m2.groups()
        dt = datetime.strptime(f"{d1} {month} {year}", "%d %B %Y").date()
        return dt.strftime("%d-%m-%Y")

    # ❗ If no pattern matches → return original value
    return original
# cleaning stages colum from tour table

word_to_num = {
    'one':1, 'two':2, 'three':3, 'four':4,
    'five':5, 'six':6, 'seven':7, 'eight':8
}

def fix_stages(x):
    x = str(x).lower()

    # base stages
    base = int(re.search(r'\d+', x).group())

    # prologue
    prologue = 1 if 'prologue' in x else 0

    # split stages
    split_match = re.search(r'including (\w+) split', x)
    split = word_to_num.get(split_match.group(1), 0) if split_match else 0

    return base + prologue + split





#----------------cleaning function for distance tours table----------------------

def extract_distance(distance_text):
    original = str(distance_text).strip()

    # Find number before 'km'
    m = re.search(r"([\d,]+\.?\d*)\s*km", original, re.IGNORECASE)
    if m:
        km_value = m.group(1).replace(",", "")
        return float(km_value)

    # If no match → keep original
    return original

# ------------------cleaning time taken col from  Winners table----------------
import re

def total_time_seconds(time_text):
    if time_text is None:
        return None

    original = str(time_text).strip().replace('"', '')

    # Case 1: HH:MM:SS
    m1 = re.match(r"(\d+):(\d{2}):(\d{2})", original)
    if m1:
        h, m, s = map(int, m1.groups())
        return h*3600 + m*60 + s

    # Case 2: 94h 33' 14
    m2 = re.search(r"(\d+)h\s*(\d+)'\s*(\d+)", original)
    if m2:
        h, m, s = map(int, m2.groups())
        return h*3600 + m*60 + s

    return None

# cleaning margin col in winners table
import re
import re

def margin_seconds(margin_text):
    if margin_text is None:
        return None

    original = str(margin_text).strip().replace('"', '').replace('+', '')

    # HH:MM:SS
    m0 = re.match(r"(\d+):(\d{2}):(\d{2})", original)
    if m0:
        h, m, s = map(int, m0.groups())
        return h*3600 + m*60 + s

    # 2h 59' 21
    m1 = re.search(r"(\d+)h\s*(\d+)'\s*(\d+)", original)
    if m1:
        h, m, s = map(int, m1.groups())
        return h*3600 + m*60 + s

    # 8' 37
    m2 = re.search(r"(\d+)'\s*(\d+)", original)
    if m2:
        m, s = map(int, m2.groups())
        return m*60 + s

    # only seconds like 55
    m3 = re.search(r"^\s*(\d+)\s*$", original)
    if m3:
        return int(m3.group(1))

    return None

def clean_avg_speed(speed_text):
    if speed_text is None:
        return None

    text = str(speed_text).strip().lower()

    # extract first decimal/number from text
    m = re.search(r"\d+\.?\d*", text)
    if m:
        return float(m.group())

    return None
# cleaning height in winners tables


def clean_height(height_text):
    if height_text is None:
        return None

    text = str(height_text).strip().lower()

    # extract decimal number
    m = re.search(r"\d+\.?\d*", text)
    if m:
        return float(m.group())

    return None

# cleaning weight in winners
import re

def clean_weight(weight_text):
    if weight_text is None:
        return None

    text = str(weight_text).strip().lower()

    # extract integer/decimal number
    m = re.search(r"\d+\.?\d*", text)
    if m:
        return float(m.group())

    return None
# cleaning distance in stages


def stage_distance(val):
    if pd.isna(val):
        return val

    text = str(val)

    # remove NBSP / encoding garbage
    text = text.replace('\xa0', ' ').replace('Â', '')

    # extract number before km
    match = re.search(r'(\d+\.?\d*)\s*km', text, re.IGNORECASE)

    if match:
        return float(match.group(1))
    else:
        # if not matching pattern, keep original
        return val



# cleaning stage type col in stages
def clean_stage_type(val):
    if pd.isna(val):
        return val

    text = str(val).strip().lower()

    # remove extra spaces and brackets like (s)
    text = re.sub(r'[\(\)]', '', text)
    text = re.sub(r'\s+', ' ', text)

    if 'plain stage' in text:
        return 'Plain Stage'

    if 'mountain time trial' in text:
        return 'Mountain Time Trial'

    if 'individual time trial' in text:
        return 'Individual Time Trial'

    if 'team time trial' in text:
        return 'Team Time Trial'

    # catches: stage with mountain, mountains, mountain(s)
    if 'mountain' in text:
        return 'Mountain Stage'

    # if something new appears, keep it as is
    return val


#clean winner from stages


def fix_encoding(text):
    try:
        return text.encode('latin1').decode('utf-8')
    except:
        return text

def extract_winner_name(val):
    if pd.isna(val):
        return val

    # Fix broken characters (RenÃ© → René)
    val = fix_encoding(str(val))

    # Remove country part (anything in brackets)
    name = re.sub(r'\s*\(.*?\)', '', val).strip()

    return name
# cleaning rider  from


def clean_rider_name(val):
    if pd.isna(val):
        return val

    val = str(val)

    # 1) Fix encoding (RenÃ© → René, FranÃ§ois → François)
    try:
        val = val.encode('latin1').decode('utf-8')
    except:
        pass

    # 2) Remove [27] references
    val = re.sub(r'\[\d+\]', '', val)

    # 3) Remove country (FRA), (BEL), (ITA) etc
    val = re.sub(r'\s*\(.*?\)', '', val)

    # 4) Remove extra spaces / weird chars
    val = val.replace('\xa0', ' ').strip()

    return val
# cleaning  time gap in finish table



def clean_timegap_seconds(val):
    if pd.isna(val):
        return None

    text = str(val)
    text = text.replace('"', '').replace('+', '').strip()
    text = re.sub(r"\s+", " ", text)

    # capture optional h, m, s
    pattern = r'(?:(\d+)\s*h)?\s*(?:(\d+)\s*\'\s*)?(?:(\d+))?'
    m = re.search(pattern, text)

    if not m:
        return None

    h = int(m.group(1)) if m.group(1) else 0
    mnt = int(m.group(2)) if m.group(2) else 0
    sec = int(m.group(3)) if m.group(3) else 0

    return h*3600 + mnt*60 + sec

# cleaning team in finish


def clean_team(text):
    if pd.isna(text) or str(text).strip().lower() == 'null':
        return None

    # Step 1: fix encoding if present
    try:
        text = text.encode('latin1').decode('utf-8')
    except:
        pass

    # Step 2: normalize dashes and weird chars
    text = re.sub(r'â..', '-', text)   # fixes â?? type junk
    text = text.replace('–', '-').replace('—', '-')

    # Step 3: remove extra spaces around dash
    text = re.sub(r'\s*-\s*', '-', text)

    # Step 4: standardize Touriste-Routier naming
    text = re.sub(r'touriste[\s\-]?routier', 'Touriste-Routier', text, flags=re.I)

    # Step 5: trim
    text = text.strip()

    return text

# for date format

def to_date(s: str) -> Optional[date]:
    """
    Convert common date string formats to datetime.date.
    Supports:
      - 'dd-MM-yyyy'
      - 'yyyy-MM-dd'
    Returns None for invalid inputs.
    """
    if not s or not isinstance(s, str):
        return None

    s = s.strip()

    for fmt in ("%d-%m-%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue

    return None
# converting to int


def to_int(value: Any) -> Optional[int]:
    try:
        if value is None:
            return None

        v = str(value).strip().lower()

        if v in {"", "null", "none", "nan"}:
            return None

        return int(float(v))   # ← important fix
    except (ValueError, TypeError):
        return None

