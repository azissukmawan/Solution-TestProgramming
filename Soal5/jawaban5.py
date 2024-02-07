import random

# mendifinisikan box
boxes = ['A', 'B', 'C', 'D', 'E']

# tempatkan objek di dalam box secara random
object_box = random.choice(boxes)

# definisikan urutan pencarian: C, B, D, A, E
search_order = ['C', 'B', 'D', 'A', 'E']

# simulasi pencarian
for step in range(7):
    # cek box selanjutnya dalam urutan pencarian
    box_to_check = search_order[step % 5]
    print(f"Step {step+1}: Checking box {box_to_check}")

    # jika objek ditemukan, berhenti pencarian
    if box_to_check == object_box:
        print(f"Object found in box {box_to_check}!")
        break

    # Jika tidak, pindahkan objek ke box yang bersebelahan (jika ada)
    object_index = boxes.index(object_box)
    if object_index > 0 and object_index < 4:
        object_box = boxes[object_index + random.choice([-1, 1])]
    elif object_index == 0:
        object_box = boxes[1]
    else:  # object_index == 4
        object_box = boxes[3]

    print(f"Object moved to box {object_box}")