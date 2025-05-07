def solution(info, n, m):
    # 1) 전체 물건 수와 A 흔적의 최대합을 계산
    k = len(info)
    total_a = sum(a for a, _ in info)  # A가 다 훔쳤을 때 남기는 흔적 총합

    # 2) DP 테이블 정의
    #    dp[a_sum][b_sum] = True 이면,
    #      “어떤 방식으로 첫 i개 물건을 훔쳐서  
    #        A 흔적이 a_sum, B 흔적이 b_sum인 상태가 가능하다”
    #    a_sum 차원은 0..total_a, b_sum 차원은 0..m-1 까지만 고려
    dp = [[False] * m for _ in range(total_a + 1)]
    dp[0][0] = True  # 아무도 훔치지 않은 상태

    # 3) 물건을 하나씩 처리하며 DP 전이
    for idx, (a_i, b_i) in enumerate(info):
        next_dp = [[False] * m for _ in range(total_a + 1)]
        for a_sum in range(total_a + 1):
            for b_sum in range(m):
                if not dp[a_sum][b_sum]:
                    continue

                # 3-1) A가 이 물건을 훔친다 → A흔적 += a_i, B흔적 그대로
                na = a_sum + a_i
                if na <= total_a:
                    next_dp[na][b_sum] = True

                # 3-2) B가 이 물건을 훔친다 → B흔적 += b_i, A흔적 그대로
                nb = b_sum + b_i
                if nb < m:
                    next_dp[a_sum][nb] = True

        dp = next_dp  # i번째 물건까지 고려된 상태로 갱신

    # 4) 모든 물건을 처리한 뒤, 가능한 상태 중에서
    #    A흔적(a_sum)이 최소인 값을 찾는다 (단, A흔적 < n 이어야 함)
    answer = None
    for a_sum in range(total_a + 1):
        if a_sum >= n:  
            # a_sum이 n 이상이면 A가 잡히므로 볼 필요 없음
            break
        for b_sum in range(m):
            if dp[a_sum][b_sum]:
                answer = a_sum
                break
        if answer is not None:
            break

    # 5) answer가 None이면 어떤 경우에도 A<n, B<m를 동시에 만족할 수 없다는 뜻
    return answer if answer is not None else -1