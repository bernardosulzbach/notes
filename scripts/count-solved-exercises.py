import sys

BEGIN_SUBSECTION = '\\subsection'
BEGIN_SUBSECTION_OF_INTEREST = '\\subsection{Solved course exercises}'
BEGIN_EXERCISE = '\\begin{Exercise}'
END_EXERCISE = '\\end{Exercise}'
BEGIN_ANSWER = '\\begin{Answer}'


def print_count(filename):
    with open(filename) as file_handler:
        capturing = False
        exercises = []
        answered = []
        for line_number, line in enumerate(file_handler, start=1):
            line = line.strip()
            if line == BEGIN_SUBSECTION_OF_INTEREST:
                capturing = True
                continue
            if capturing:
                if line.startswith(BEGIN_SUBSECTION):
                    capturing = False
                elif line.startswith(BEGIN_EXERCISE):
                    if len(answered) < len(exercises):
                        answered.append(False)
                    exercises.append(line_number)
                elif line.startswith(BEGIN_ANSWER):
                    answered.append(True)
        if len(answered) < len(exercises):
            answered.append(False)
        answer_count = answered.count(True)
        exercise_count = len(exercises)
        print('Found {} exercises. {} are answered.'.format(exercise_count, answer_count))
        for i, line in enumerate(exercises):
            if not answered[i]:
                print('Missing answer at line {}.'.format(line))
        print('Completion is {:.1f}%.'.format(100.0 * answer_count / exercise_count))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {} [FILENAME]'.format(sys.argv[0]))
    else:
        print_count(sys.argv[1])
