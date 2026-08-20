class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for x in asteroids:

            while st and st[-1] > 0 and x < 0:

                if st[-1] < abs(x):
                    st.pop()
                    continue

                elif st[-1] == abs(x):
                    st.pop()

                break

            else:
                st.append(x)

        return st