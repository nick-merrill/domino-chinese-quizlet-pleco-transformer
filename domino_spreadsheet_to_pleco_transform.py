# Transform Domino Chinese vocabulary spreadsheet into Pleco format.
#
# Specify the input file with the first argument when calling the script.
#

import csv
import sys

# The super-category to encapsulate all these cards.
BRAND_CATEGORY = "DominoChinese.com"


def main():
    with open(sys.argv[1]) as csv_file:
        reader = csv.reader(csv_file)
        output_pleco_format(reader)


def output_pleco_format(csv_reader):
    """Reads the CSV format and writes the Pleco format to stdout.
    """
    level = None
    lesson = None
    for row_num, row in enumerate(csv_reader):
        if row[0] == "":
            # Skip blank rows.
            continue
        if row[0].startswith("Level"):
            # Set the level name for the upcoming rows.
            level = row[0]
            # Unset the lesson name.
            lesson = None
            continue
        if row[0].startswith("Lesson"):
            # Set the lesson name for the upcoming rows.
            lesson = row[0]
            # Output the deepest sub-category string.
            sys.stdout.write("{}\n".format(
                get_category_string(level=level, lesson=lesson)
            ))
            continue
        # Otherwise we are actually looking at a flashcard item that belongs
        # to a lesson and level.
        # Ensure the level and lesson are already set for this card.
        if None in [level, lesson]:
            raise ValueError(
                "Every card must be part of a level and lesson. "
                "(Failed on row {}.)".format(row_num)
            )
        characters, pinyin, english = row
        sys.stdout.write("{characters}\t{pinyin}\t{english}\n".format(
            characters=characters,
            pinyin=pinyin,
            english=english,
        ))


def get_category_string(level: str, lesson: str) -> str:
    """Returns the Pleco-formatted category string.

    Pleco requires the category string to start with a double-slash,
    followed by the category and subcategory names separated by slashes.
    """
    return "//{brand_category}/{level}/{lesson}".format(
        brand_category=BRAND_CATEGORY,
        level=level,
        lesson=lesson,
    )


if __name__ == "__main__":
    main()
