from typing import List, Dict, Any

AnswerObj = Dict[str, Any]

def choose_semester(dataset: List[AnswerObj]) -> int:
    semesters = sorted({
        obj["semester"]
        for obj in dataset
        if "semester" in obj
    })

    if not semesters:
        raise ValueError("No semester field found in dataset")

    print("\nAvailable Semesters:")
    for i, sem in enumerate(semesters, start=1):
        print(f"{i}. Semester {sem}")

    while True:
        try:
            choice = int(input("Select semester number: "))
            if 1 <= choice <= len(semesters):
                return semesters[choice - 1]
        except ValueError:
            pass
        print("Invalid selection. Try again.")

def choose_subject(dataset: List[AnswerObj]) -> str:
    subjects = sorted({
        obj["subject"]
        for obj in dataset
        if "subject" in obj
    })

    print("\nAvailable Subjects:")
    for i, sub in enumerate(subjects, start=1):
        print(f"{i}. {sub}")

    while True:
        try:
            choice = int(input("Select subject number: "))
            if 1 <= choice <= len(subjects):
                return subjects[choice - 1]
        except ValueError:
            pass
        print("Invalid selection. Try again.")
