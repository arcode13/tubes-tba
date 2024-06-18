class FiniteAutomata:
    def __init__(self, valid_tokens):
        self.valid_tokens = valid_tokens

    def recognize(self, word):
        return word in self.valid_tokens

class PushdownAutomata:
    def __init__(self, s_recognizer, p_recognizer, o_recognizer, k_recognizer):
        self.s_recognizer = s_recognizer
        self.p_recognizer = p_recognizer
        self.o_recognizer = o_recognizer
        self.k_recognizer = k_recognizer

    def parse(self, tokens):
        state = 'S'
        structure = []

        for token in tokens:
            if state == 'S':
                if self.s_recognizer.recognize(token):
                    structure.append('S')
                    state = 'P'
                else:
                    return False, structure
            elif state == 'P':
                if self.p_recognizer.recognize(token):
                    structure.append('P')
                    state = 'O'
                else:
                    return False, structure
            elif state == 'O':
                if self.o_recognizer.recognize(token):
                    structure.append('O')
                    state = 'K'
                else:
                    if self.k_recognizer.recognize(token):
                        structure.append('K')
                        state = 'END'
                    else:
                        return False, structure
            elif state == 'K':
                if self.k_recognizer.recognize(token):
                    structure.append('K')
                    state = 'END'
                else:
                    return False, structure

        valid_patterns = [['S', 'P', 'O', 'K'], ['S', 'P', 'K'], ['S', 'P', 'O'], ['S', 'P']]
        return structure in valid_patterns, structure

def print_tokens(title, tokens):
    print(f"{title:^50}")
    print('-'*50)
    for i, token in enumerate(tokens, 1):
        print(f'{token:<10}', end=' ')
        if i % 4 == 0:
            print()
    print("\n")

def print_valid_patterns():
    valid_patterns = [
        "1. S - P - O - K",
        "2. S - P - O",
        "3. S - P - K",
        "4. S - P"
    ]
    print("="*50)
    print(f"{'POLA YANG VALID':^50}")
    print("\n")
    for pattern in valid_patterns:
        print(f'{pattern:<35} [✓]')

def main():
    subjek_tokens = ["saya", "kamu", "dia", "mereka", "kita", "aku"]
    predikat_tokens = ["makan", "minum", "baca", "tulis", "lari"]
    objek_tokens = ["nasi", "air", "buku", "surat", "sepeda"]
    keterangan_tokens = ["dirumah", "disekolah", "dikantor", "dipasar", "ditaman"]

    s_recognizer = FiniteAutomata(subjek_tokens)
    p_recognizer = FiniteAutomata(predikat_tokens)
    o_recognizer = FiniteAutomata(objek_tokens)
    k_recognizer = FiniteAutomata(keterangan_tokens)

    parser = PushdownAutomata(s_recognizer, p_recognizer, o_recognizer, k_recognizer)

    print("\n")
    print("="*50)
    print(f"{'TUBES TEORI BAHASA DAN AUTOMATA':^50}")
    print("\n")
    print(f"{'Anggota Kelompok':^50}")
    print("\n")
    print(f"{'Muh. Syahrul Minanul Aziz':<35} | {'1301223369':>12}")
    print(f"{'Muhammad Rafi Raihan Akbar':<35} | {'1301223219':>12}")
    print(f"{'Khairani Razita Putri':<35} | {'1301223373':>12}")
    print("="*50)
    print("\n")

    print("="*50)
    print(f"{'KATA KUNCI':^50}")
    print("="*50)
    print("\n")
    print_tokens("SUBJEK", subjek_tokens)
    print_tokens("PREDIKAT", predikat_tokens)
    print_tokens("OBJEK", objek_tokens)
    print_tokens("KETERANGAN", keterangan_tokens)
    print("="*50)
    print("\n")

    print_valid_patterns()
    print("="*50)
    print("\n")

    sentence = input("Masukkan Kalimat : ")
    tokens = sentence.split()
    is_valid, structure = parser.parse(tokens)
    
    print("\n")
    print("="*50)
    print(f"{'HASIL':^50}")
    print("\n")
    print(f"{'Kalimat:':<10} {sentence}")
    print(f"{'Struktur:':<10} {' '.join(structure)}")
    print(f"{'Valid:':<10} {is_valid}")
    print("="*50)

if __name__ == '__main__':
    main()