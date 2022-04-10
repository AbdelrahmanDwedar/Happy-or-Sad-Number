# Happy 😄 or Sad 😞 Numbers 🔢

This is the solve of the famous **[Google](https://www.google.com/)** interview question **find the happy number**.
It's a function that called `HappyOrSad()` that finds out if the number is **happy** or **sad** number.

---

## What is Happy number ❓

### It is a number that if you added their squared digits to each other and repeat the same progress to the result again and again it'll give `1` in the end.

**E.X.**

> 19 -> 1<sup>2</sup> + 9<sup>2</sup> = 82  
> 82 -> 8<sup>2</sup> + 2<sup>2</sup> = 68  
> 68 -> 6<sup>2</sup> + 8<sup>2</sup> = 100  
> 100 -> 1<sup>2</sup> + ~~0<sup>2</sup>~~ + ~~0<sup>2</sup>~~ = 1  

### on the other hand a sad number (unhappy number) is a number that falls into a loop of repeating itself when we do the same for it. 

**E.x.**

> 2 -> 2<sup>2</sup> = 4
> 4 -> 4<sup>2</sup> = 8
> 8 -> 8<sup>2</sup> = 16
> 16 -> 1<sup>2</sup> + 6<sup>2</sup> = 37
> 37 -> 3<sup>2</sup> + 7<sup>2</sup> = 58
> 58 -> 5<sup>2</sup> + 8<sup>2</sup> = 89
> 89 -> 8<sup>2</sup> + 9<sup>2</sup> = 145
> 145 -> 1<sup>2</sup> + 4<sup>2</sup> + 5<sup>2</sup> = 42
> 42 -> 4<sup>2</sup> + 2<sup>2</sup> = 20
> 20 -> 2<sup>2</sup> + ~~0<sup>2</sup>~~ = 4 (again)

If you noticed the `4` repeated itself again, and the same prosses will happen everytime in infinite loop of times.

---

#### Yotube videos:-

- https://youtu.be/Te1GoYWKmz8

- inspired by: https://youtube.ckom/shorts/5FC__K2dRoQ?feature=share 

---

<h2 align="center">Upcoming more ways<b>...</b></h2>
