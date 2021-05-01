<main class="col-md">

<h1 id="knights">Knights</h1>

<p>Write a program to solve logic puzzles.</p>

<h2 id="background">Background</h2>

<p>In 1978, logician Raymond Smullyan published “What is the name of this book?”, a book of logical puzzles. Among the puzzles in the book were a class of puzzles that Smullyan called “Knights and Knaves” puzzles.</p>

<p>In a Knights and Knaves puzzle, the following information is given: Each character is either a knight or a knave. A knight will always tell the truth: if knight states a sentence, then that sentence is true. Conversely, a knave will always lie: if a knave states a sentence, then that sentence is false.</p>

<p>The objective of the puzzle is, given a set of sentences spoken by each of the characters, determine, for each character, whether that character is a knight or a knave.</p>

<p>For example, consider a simple puzzle with just a single character named A. A says “I am both a knight and a knave.”</p>

<p>Logically, we might reason that if A were a knight, then that sentence would have to be true. But we know that the sentence cannot possibly be true, because A cannot be both a knight and a knave – we know that each character is either a knight or a knave, but not both. So, we could conclude, A must be a knave.</p>

<p>That puzzle was on the simpler side. With more characters and more sentences, the puzzles can get trickier! Your task in this problem is to determine how to represent these puzzles using propositional logic, such that an AI running a model-checking algorithm could solve these puzzles for us.</p>

<h2 id="getting-started">Getting Started</h2>

<ul>
  <li data-marker="*">Download the distribution code from <a href="https://cdn.cs50.net/ai/2020/x/projects/1/knights.zip">https://cdn.cs50.net/ai/2020/x/projects/1/knights.zip</a> and unzip it.</li>
</ul>

<h2 id="understanding">Understanding</h2>

<p>Take a look at <code class="language-plaintext highlighter-rouge">logic.py</code>, which you may recall from Lecture 1. No need to understand everything in this file, but notice that this file defines several classes for different types of logical connectives. These classes can be composed within each other, so an expression like <code class="language-plaintext highlighter-rouge">And(Not(A), Or(B, C))</code> represents the logical sentence stating that symbol <code class="language-plaintext highlighter-rouge">A</code> is not true, and that symbol <code class="language-plaintext highlighter-rouge">B</code> or symbol <code class="language-plaintext highlighter-rouge">C</code> is true (where “or” here refers to inclusive, not exclusive, or).</p>

<p>Recall that <code class="language-plaintext highlighter-rouge">logic.py</code> also contains a function <code class="language-plaintext highlighter-rouge">model_check</code>. <code class="language-plaintext highlighter-rouge">model_check</code> takes a knowledge base and a query. The knowledge base is a single logical sentence: if multiple logical sentences are known, they can be joined together in an <code class="language-plaintext highlighter-rouge">And</code> expression. <code class="language-plaintext highlighter-rouge">model_check</code> recursively considers all possible models, and returns <code class="language-plaintext highlighter-rouge">True</code> if the knowledge base entails the query, and returns <code class="language-plaintext highlighter-rouge">False</code> otherwise.</p>

<p>Now, take a look at <code class="language-plaintext highlighter-rouge">puzzle.py</code>. At the top, we’ve defined six propositional symbols. <code class="language-plaintext highlighter-rouge">AKnight</code>, for example, represents the sentence that “A is a knight,” while <code class="language-plaintext highlighter-rouge">AKnave</code> represents the sentence that “A is a knave.” We’ve similarly defined propositional symbols for characters B and C as well.</p>

<p>What follows are four different knowledge bases, <code class="language-plaintext highlighter-rouge">knowledge0</code>, <code class="language-plaintext highlighter-rouge">knowledge1</code>, <code class="language-plaintext highlighter-rouge">knowledge2</code>, and <code class="language-plaintext highlighter-rouge">knowledge3</code>, which will contain the knowledge needed to deduce the solutions to the upcoming Puzzles 0, 1, 2, and 3, respectively. Notice that, for now, each of these knowledge bases is empty. That’s where you come in!</p>

<p>The <code class="language-plaintext highlighter-rouge">main</code> function of this <code class="language-plaintext highlighter-rouge">puzzle.py</code> loops over all puzzles, and uses model checking to compute, given the knowledge for that puzzle, whether each character is a knight or a knave, printing out any conclusions that the model checking algorithm is able to make.</p>

<h2 id="specification">Specification</h2>

<div class="alert" data-alert="warning" role="alert"><p>An automated tool assists the staff in enforcing the constraints in the below specification. Your submission will fail if any of these are not handled properly, if you import modules other than those explicitly allowed, or if you modify functions other than as permitted.</p></div>

<p>Add knowledge to knowledge bases <code class="language-plaintext highlighter-rouge">knowledge0</code>, <code class="language-plaintext highlighter-rouge">knowledge1</code>, <code class="language-plaintext highlighter-rouge">knowledge2</code>, and <code class="language-plaintext highlighter-rouge">knowledge3</code> to solve the following puzzles.</p>

<ul>
  <li data-marker="*">Puzzle 0 is the puzzle from the Background. It contains a single character, A.
    <ul>
      <li data-marker="*">A says “I am both a knight and a knave.”</li>
    </ul>
  </li>
  <li data-marker="*">Puzzle 1 has two characters: A and B.
    <ul>
      <li data-marker="*">A says “We are both knaves.”</li>
      <li data-marker="*">B says nothing.</li>
    </ul>
  </li>
  <li data-marker="*">Puzzle 2 has two characters: A and B.
    <ul>
      <li data-marker="*">A says “We are the same kind.”</li>
      <li data-marker="*">B says “We are of different kinds.”</li>
    </ul>
  </li>
  <li data-marker="*">Puzzle 3 has three characters: A, B, and C.
    <ul>
      <li data-marker="*">A says either “I am a knight.” or “I am a knave.”, but you don’t know which.</li>
      <li data-marker="*">B says “A said ‘I am a knave.’”</li>
      <li data-marker="*">B then says “C is a knave.”</li>
      <li data-marker="*">C says “A is a knight.”</li>
    </ul>
  </li>
</ul>

<p>In each of the above puzzles, each character is either a knight or a knave. Every sentence spoken by a knight is true, and every sentence spoken by a knave is false.</p>

<p>Once you’ve completed the knowledge base for a problem, you should be able to run <code class="language-plaintext highlighter-rouge">python puzzle.py</code> to see the solution to the puzzle.</p>

<h2 id="hints">Hints</h2>

<ul>
  <li data-marker="*">For each knowledge base, you’ll likely want to encode two different types of information: (1) information about the structure of the problem itself (i.e., information given in the definition of a Knight and Knave puzzle), and (2) information about what the characters actually said.</li>
  <li data-marker="*">Consider what it means if a sentence is spoken by a character. Under what conditions is that sentence true? Under what conditions is that sentence false? How can you express that as a logical sentence?</li>
  <li data-marker="*">There are multiple possible knowledge bases for each puzzle that will compute the correct result. You should attempt to choose a knowledge base that offers the most direct translation of the information in the puzzle, rather than performing logical reasoning on your own. You should also consider what the most concise representation of the information in the puzzle would be.
    <ul>
      <li data-marker="*">For instance, for Puzzle 0, setting <code class="language-plaintext highlighter-rouge">knowledge0 = AKnave</code> would result in correct output, since through our own reasoning we know A must be a knave. But doing so would be against the spirit of this problem: the goal is to have your AI do the reasoning for you.</li>
    </ul>
  </li>
  <li data-marker="*">You should not need to (nor should you) modify <code class="language-plaintext highlighter-rouge">logic.py</code> at all to complete this problem.</li>
</ul>

</main>