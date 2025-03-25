---
layout: default
title: Proof of Godel's incompleteness Theorem
---

# Proof of Godel's incompleteness Theorem

## Gödel's proof in simple English:

Gödel found a statement in mathematics that had 2 layers of meaning. On first layer, it was claiming that a numbers, lets call it $a$, had a specific complicated property. On the other layer of meaning, the statement was essentially saying it cannot be proven using the present axioms of mathematics that you started with. The statement is referring to itself while making a claim! Self reference!

So, is the claim, that $a$ has the mentioned property, true or false? If it is false, then by using second layer of meaning, you could prove that the statement, and hence it must be true, which implies that $a$ has the mentioned property! So, if the statement is false, then it is true! But this is inconsistent!

On the other hand, if the statement is assumed to be true, then by the second layer of meaning, it would be proven to be not provable by your current mathematical toolbox. Essentially, the statement would be a new axiom that needs to be added to your toolbox of mathematics. But with this more powerful toolbox, we again run into the same problem. There would be a new statement which is again beyond this new toolbox.


## Delving deeper into Gödel's proof, but still in simple English:

Now, let's talk a little more about how Gödel did it.

In order to create the situation of self reference, Gödel first started with mathematically studying the process of doing mathematics! This is called Metamathematics.

Gödel noted that all mathematical claims use some limited set of symbols. But not all collections of symbols are equally meaningful in mathematics. So, he first set up a 'grammar' to rule out grammatically nonsensical collection of symbols. For example, in the following three collection of symbols: 
  1. $6=7$,
  1. $14= 7\times 2$ and
  1. $67/ \times \times 52 \div$,

the first two are grammatically correct, but the first one is false, while second one is true. Whereas, the 3rd collection of symbols is grammatically incorrect! We are only interested in finding out whether collection of symbols that are grammatically correct are also logically correct or not. Hence, from now on, we will call collection of symbols that are grammatically correct as 'statements'.

Now, in his framework, he developed a scheme to assign all statements in mathematics, true or false, a unique number, which we will call the Gödel number of that statement.

In mathematics, we start with some statements that we assume to be true and call them axioms. We also device some precise rules to logically infer the truth of new statements given some old ones.

Now, mathematically studying mathematics involves studying that if statement C follows logically from statement A and B, then the corresponding numbers that Gödel assigned them will be related in a precise way.

Gödel also assigned a string of mathematical statements a unique number. String of statements is important in mathematics because when you are trying to prove something, you use a string of statements that follow logically from the statements before them and end up proving the final statement.

Now, again the fact that a given string of statement is a valid proof of another statement indicates that the corresponding unique numbers are related in a precise manner. Also, the fact that a given string of statements DOES NOT prove a given statement also indicates that the corresponding numbers DO NOT have the precise relation. Lastly, the fact that a statement cannot be proven by your axioms AT ALL also says that the corresponding number has a precise mathematical property, let us call it the property of being an unprovable number. Now, a number can be 'unprovable number' in the same sense that a number can be 'prime number' or 'odd number' or 'even number'. It just means that the number falls in a specific mathematical category.

Now, consider a mathematical statement that claims that a given number, $a$, is an 'unprovable number'. Now, imagine what will happen if, just by chance, the mathematical statement that claims that $a$ is an unprovable number, has a Gödel number equal to $a$.

On one layer of meaning, the mathematical statement is just claiming that an obscure number $a$ has an obscure property. On another layer of meaning, it is saying that your current axioms of mathematics are incapable of proving the statement. So, if the statement is false, then $a$ is NOT an unprovable number, which means the statement CAN be proven and is true, which means that $a$ is an unprovable number, because this is what the statement is saying! Contradiction!

So, the only possibility is that the statement is actually true, which means $a$ is an unprovable number, which means that the statement cannot be proven using the present toolbox, although it is true!

Gödel demonstrated, given any axiomatic system of mathematics that was powerful enough to describe numbers, a method to come up with a mathematical statement with Gödel number $a$ which was also claiming that $a$ is an 'unprovable number'. Hence any mathematical system that is powerful enough to describe numbers is incomplete.


## Delving deeper still into Gödel's proof, but with some mathematical notations


This proof borrows from the book 'Godel's proof' by Nagel and Newman. This post provides a very short summary of Gödel's proof, and should not make any sense in first exposure to the theorems. Any word that you do not understand can be looked up in the book I mentioned, which is an excellent source to learn about of Gödel's theorem, and is at the same time quite rigorous.
First Incompleteness theorem:
The first incompleteness theorem states that 'Any consistent formal system F within which a certain amount of elementary arithmetic can be carried out is incomplete; i.e., there are statements of the language of F which can neither be proved nor disproved in F.'

  - Uniquely number every theorem in a system of mathematics. We can do this by assigning 10 symbols like $0$,$1$,$\subset$ (short for ‘if . . . then . . .’) etc a number between 1 to 10. Also, we can assign numerical variables, sentential variables and predicate variables to first, second and third powers of prime numbers greater or equal to 11, respectively. Note that the use of prime number ensures that all these variables get assigned a unique number, because otherwise $11^2$ is nothing but 121. Another way of doing it could have been assigning 11, 12 and 13 with variable of each type sequentially, and then repeat for 14,15 and 16 etc. If you don't understand what I mean here, never mind. Just another way to do the same thing.
  - Now that each letter of the language has a unique numerical representation, we assign a number to a formula by raising the nth prime to the power of the numerical value of the nth symbol, and taking product of all such numbers. Strings of formulas separated by comma is also a formula.
  - The fact that a formula with Gödel number x is the proof of a Gödel number z hints towards a mathematical property that these two numbers share in the general case. This mathematical property depends upon the syntax as well as the rule of inference of the proof system. Let us denote the fact that the numbers x and z share this specific property by the formula $ Dem(x,z)$. This formula might not be true for a given value of x and z. Note that here, $Dem$ is a predicate variable.
  - Next, let $sub(m,13,m)$ denote the Gödel number of the formula that you get when you replace in the formula with Gödel number m, each occurrence of the variable with Gödel number 13 (here y) the number m.
  - Now, note the meaning of $\sim \exists x Dem(x,sub(n,13,n))$ where n is Gödel number of the statement $\sim \exists x Dem(x,sub(y,13,y))$. Note that $sub(n,13,n)$ is just the Gödel number of the first formula. Hence, the first formula states that it cannot be proven within the system. (Although seen at mathematical level, the first formula just claims that a number does not have a given mathematical property. It is only when interpreted at metamathematical level that we infer a second layer of meaning to this statement- that it is claiming that it cannot be proven within the system). Now, if this statement is false, then it can be proven. A system of mathematics that can prove even false results is inconsistent. Hence, it must be true, and hence cannot be proven.
  - Note that $\sim \exists x Dem(x,sub(n,13,n))$ expresses a property that no number possesses. Hence, it represents a new axiom of mathematics.


Notes:-

  - If there are finitely many rules of inference, then Gödel's theorem holds. If there are infinitely many of them, then we get another Gödel like situation, where instead of infinite axioms, there infinite rules of inference. But the question is, is there an equivalent formulation of logic where there are only axioms but no rule of inference? I don't think so. Rules of inference are necessary to get from one axiom to another. They can be encompassed by a property that Gödel numbers possess, as given by $Dem(x,z)$. Hence the rules of inference link numbers based on some property. Gödel statement of a system of axioms is a statement that numbers don't possess a certain property.
  - How does the choice of syntax affect the numerical relations as in $Dem(x,z)$? There should be some invariance regarding some general properties of these relations, independent of the choice of syntax.

# Second Incompleteness theorem

The second incompleteness theorem states that 'Assume F is a consistent formalized system which contains elementary arithmetic. Then the consistency of F is not provable within F.'

The proof of the second incompleteness theorem follows from the first one. Even though the Gödel statement G of a system F states that it is not provable, the reason why we cannot prove it within the system is that we are assuming that our system is consistent, and hence cannot prove a statement which says that it is not provable. Hence the consistency of F implies its incompleteness. The last sentence itself can be formalized as a theorem in F, and can also be proven within F. The proof follows because if we know that our system is consistent, then there is no more barrier in proving that G must be true. It is the lack of proof of consistency that prevents a proof a G. But if G is proven, then we will get an absurd result. Hence if F is consistent, its consistency itself is necessarily not provable to establish the non-provability of G.
