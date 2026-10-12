import pandas as pd

#=============================
#  Read Squid data function  #
#=============================
def read_squid_file(filepath: str) -> pd.DataFrame:
    """
    A function for reading in Squid Files 

    kwargs:
    filepath -- the string filepath for the dataframe
    """
    with open(filepath, encoding="utf-8", errors="replace") as f:
        skip = next(
            i for i, line in enumerate(f, start=1) if line.strip() == "[Data]"
        )

    df = pd.read_csv(
        filepath,
        skiprows=skip,
        na_values=["No data", "NaN", "", " ", "  ", "m"],
    )

    df = df.drop(
        columns=[
            "Comment",
            "Averaging Time (sec)",
            "Frequency (Hz)",
            "Peak Amplitude (mm)",
            "Lockin Signal' (V)",
            "Lockin Signal (V)",
            "Range",
            "M. Quad. Signal (emu)",
            "AC Moment (emu)",
            "AC M. Std Err. (emu)",
            "AC Phase (deg)",
            "AC Phase Std. Err. (deg)",
            "Map 01",
            "Map 02",
            "Map 03",
            "Map 04",
            "Map 05",
            "Map 06",
            "Map 07",
            "Map 08",
            "Map 09",
            "Map 10",
            "Map 11",
            "Map 12",
            "Map 13",
            "Map 14",
            "Map 15",
            "Map 16",
        ]
    )
    return df