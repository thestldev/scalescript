import json

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

scales = {
    "Major (Ionian)": [0, 2, 4, 5, 7, 9, 11],
    "Major Bebop": [0, 2, 4, 5, 7, 8, 9, 11],
    "Major Bulgarian": [0, 1, 4, 5, 7, 8, 11],
    "Major Hexatonic": [0, 2, 4, 5, 7, 9],
    "Major Pentatonic": [0, 2, 4, 7, 9],
    "Major Persian": [0, 1, 4, 5, 6, 8, 11],
    "Major Polymode": [0, 2, 4, 5, 7, 8, 9, 10, 11],
    "Minor Harmonic": [0, 2, 3, 5, 7, 8, 11],
    "Minor Hungarian": [0, 2, 3, 6, 7, 8, 11],
    "Minor Melodic": [0, 2, 3, 5, 7, 9, 11],
    "Minor Natural (Aeolian)": [0, 2, 3, 5, 7, 8, 10],
    "Minor Neapolitan": [0, 1, 3, 5, 7, 8, 11],
    "Minor Pentatonic": [0, 3, 5, 7, 10],
    "Minor Polymode": [0, 2, 3, 5, 7, 8, 9, 10, 11],
    "Minor Romanian": [0, 2, 3, 6, 7, 9, 10],
    "Other Arabic": [0, 1, 4, 5, 7, 8, 11],
    "Other Bebop Dominant": [0, 2, 4, 5, 7, 9, 10, 11],
    "Other Blues": [0, 3, 5, 6, 7, 10],
    "Other Blues Nonatonic": [0, 2, 3, 4, 5, 6, 7, 9, 10],
    "Other Diminished": [0, 2, 3, 5, 6, 8, 9, 11],
    "Other Dorian": [0, 2, 3, 5, 7, 9, 10],
    "Other Eastern": [0, 1, 4, 5, 6, 8, 10],
    "Other Egyptian": [0, 2, 5, 7, 10],
    "Other Enigmatic": [0, 1, 4, 6, 8, 10, 11],
    "Other Hirajoshi": [0, 2, 3, 7, 8],
    "Other Iwato": [0, 1, 5, 6, 10],
    "Other Japanese Insen": [0, 1, 5, 7, 10],
    "Other Locrian": [0, 1, 3, 5, 6, 8, 10],
    "Other Locrian Super": [0, 1, 3, 4, 6, 8, 10],
    "Other Lydian": [0, 2, 4, 6, 7, 9, 11],
    "Other Mixolydian": [0, 2, 4, 5, 7, 9, 10],
    "Other Neapolitan": [0, 1, 3, 5, 7, 9, 11],
    "Other Phrygian": [0, 1, 3, 5, 7, 8, 10],
    "Other Phrygian Dominant": [0, 1, 4, 5, 7, 8, 10],
    "Other Piongio": [0, 2, 5, 7, 9],
    "Other Prometheus": [0, 2, 4, 6, 9, 10],
    "Other Whole Tone": [0, 2, 4, 6, 8, 10]
}


def main():
    result = {note: [] for note in notes}

    for root_idx, root_note in enumerate(notes):
        for scale_name, intervals in scales.items():
            scale_full_name = f"{root_note} {scale_name}"

            for interval in intervals:
                note_idx = (root_idx + interval) % 12
                target_note = notes[note_idx]

                result[target_note].append(scale_full_name)

    for note in result:
        result[note].sort()

    # print(json.dumps(result, indent=2, ensure_ascii=False))

    with open("fl_scales.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
