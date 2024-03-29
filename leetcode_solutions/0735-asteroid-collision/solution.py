class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        popped=False
        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
            elif asteroid >= 0:
                stack.append(asteroid)
            elif asteroid <0 and stack[-1]<0:
                stack.append(asteroid)
            elif asteroid < 0:
                while stack:
                    if stack[-1]>=0:
                        condition=True if abs(asteroid)>=stack[-1] else False
                        if condition:
                            popped=stack.pop()
                            if popped==abs(asteroid):
                                break
                        else:
                            break
                    else:
                        stack.append(asteroid)
                        break

                if not stack and abs(asteroid)!=popped:
                    stack.append(asteroid)

        return stack
            
