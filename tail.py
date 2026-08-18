def func(i, N):
    if i > N:
        return
    func(i+1, N)
    print(N-i+1)
func(1, 5)