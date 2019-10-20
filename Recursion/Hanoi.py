def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

# 원판의 수, 시작 기둥, 끝 기둥.
def hanoi(num_disks, start_peg, end_peg):
    # 코드를 입력하세요.
    if num_disks == 0:
        return

    other_peg = 6 - start_peg - end_peg
    hanoi(num_disks - 1, start_peg, other_peg)
    move_disk(num_disks, start_peg, end_peg)
    hanoi(num_disks - 1, other_peg, end_peg)

# 1. 가장 큰 원판을 제외하고 나머지 원판들을 start_peg에서 other_peg로 이동
# 2. 가장 큰 원판을 start_peg에서 end_peg로 이동
# 3. 나머지 원판들을 other_peg에서 end_peg로 이동

# 테스트 코드 (포함하여 제출해주세요)
#hanoi(1, 1, 3)
#hanoi(2, 1, 3)
hanoi(3, 1, 3)

#hanoi(3, 1, 3) hanoi(2, 1, 2), hanoi(1, 1, 3) hanoi(1, 3, 2) hanoi(2, 2, 3) hanoi(1, 2, 1) hanoi(1, 1, 3) 순으로 실행.

# 원판이 2개일 때.
# 1번 원판을 1번 기둥에서 2번 기둥으로 이동
# 2번 원판을 1번 기둥에서 3번 기둥으로 이동
# 1번 원판을 2번 기둥에서 3번 기둥으로 이동

# 원판이 3개일 때.
# 1번 원판을 1번 기둥에서 3번 기둥으로 이동
# 2번 원판을 1번 기둥에서 2번 기둥으로 이동
# 1번 원판을 3번 기둥에서 2번 기둥으로 이동
# 3번 원판을 1번 기둥에서 3번 기둥으로 이동
# 1번 원판을 2번 기둥에서 1번 기둥으로 이동
# 2번 원판을 2번 기둥에서 3번 기둥으로 이동
# 1번 원판을 1번 기둥에서 3번 기둥으로 이동