<main class="col-md">

<h1 id="tic-tac-toe">Tic-Tac-Toe</h1>

<p>Using Minimax, implement an AI to play Tic-Tac-Toe optimally.</p>

<p><img src="https://cs50.harvard.edu/ai/2020/projects/0/tictactoe/images/game.png" alt="Tic-Tac-Toe Game"></p>

<h2 id="getting-started">Getting Started</h2>

<ul>
  <li data-marker="*">Download the distribution code from <a href="https://cdn.cs50.net/ai/2020/x/projects/0/tictactoe.zip">https://cdn.cs50.net/ai/2020/x/projects/0/tictactoe.zip</a> and unzip it.</li>
  <li data-marker="*">Once in the directory for the project, run <code class="language-plaintext highlighter-rouge">pip3 install -r requirements.txt</code> to install the required Python package (<code class="language-plaintext highlighter-rouge">pygame</code>) for this project.</li>
</ul>

<h2 id="understanding">Understanding</h2>

<p>There are two main files in this project: <code class="language-plaintext highlighter-rouge">runner.py</code> and <code class="language-plaintext highlighter-rouge">tictactoe.py</code>. <code class="language-plaintext highlighter-rouge">tictactoe.py</code> contains all of the logic for playing the game, and for making optimal moves. <code class="language-plaintext highlighter-rouge">runner.py</code> has been implemented for you, and contains all of the code to run the graphical interface for the game. Once you’ve completed all the required functions in <code class="language-plaintext highlighter-rouge">tictactoe.py</code>, you should be able to run <code class="language-plaintext highlighter-rouge">python runner.py</code> to play against your AI!</p>

<p>Let’s open up <code class="language-plaintext highlighter-rouge">tictactoe.py</code> to get an understanding for what’s provided. First, we define three variables: <code class="language-plaintext highlighter-rouge">X</code>, <code class="language-plaintext highlighter-rouge">O</code>, and <code class="language-plaintext highlighter-rouge">EMPTY</code>, to represent possible moves of the board.</p>

<p>The function <code class="language-plaintext highlighter-rouge">initial_state</code> returns the starting state of the board. For this problem, we’ve chosen to represent the board as a list of three lists (representing the three rows of the board), where each internal list contains three values that are either <code class="language-plaintext highlighter-rouge">X</code>, <code class="language-plaintext highlighter-rouge">O</code>, or <code class="language-plaintext highlighter-rouge">EMPTY</code>.
What follows are functions that we’ve left up to you to implement!</p>

<h2 id="specification">Specification</h2>

<div class="alert" data-alert="warning" role="alert"><p>An automated tool assists the staff in enforcing the constraints in the below specification. Your submission will fail if any of these are not handled properly, if you import modules other than those explicitly allowed, or if you modify functions other than as permitted.</p></div>

<p>Complete the implementations of <code class="language-plaintext highlighter-rouge">player</code>, <code class="language-plaintext highlighter-rouge">actions</code>, <code class="language-plaintext highlighter-rouge">result</code>, <code class="language-plaintext highlighter-rouge">winner</code>, <code class="language-plaintext highlighter-rouge">terminal</code>, <code class="language-plaintext highlighter-rouge">utility</code>, and <code class="language-plaintext highlighter-rouge">minimax</code>.</p>

<ul>
  <li data-marker="*">The <code class="language-plaintext highlighter-rouge">player</code> function should take a <code class="language-plaintext highlighter-rouge">board</code> state as input, and return which player’s turn it is (either <code class="language-plaintext highlighter-rouge">X</code> or <code class="language-plaintext highlighter-rouge">O</code>).
    <ul>
      <li data-marker="*">In the initial game state, <code class="language-plaintext highlighter-rouge">X</code> gets the first move. Subsequently, the player alternates with each additional move.</li>
      <li data-marker="*">Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).</li>
    </ul>
  </li>
  <li data-marker="*">The <code class="language-plaintext highlighter-rouge">actions</code> function should return a <code class="language-plaintext highlighter-rouge">set</code> of all of the possible actions that can be taken on a given board.
    <ul>
      <li data-marker="*">Each action should be represented as a tuple <code class="language-plaintext highlighter-rouge">(i, j)</code> where <code class="language-plaintext highlighter-rouge">i</code> corresponds to the row of the move (<code class="language-plaintext highlighter-rouge">0</code>, <code class="language-plaintext highlighter-rouge">1</code>, or <code class="language-plaintext highlighter-rouge">2</code>) and <code class="language-plaintext highlighter-rouge">j</code> corresponds to which cell in the row corresponds to the move (also <code class="language-plaintext highlighter-rouge">0</code>, <code class="language-plaintext highlighter-rouge">1</code>, or <code class="language-plaintext highlighter-rouge">2</code>).</li>
      <li data-marker="*">Possible moves are any cells on the board that do not already have an <code class="language-plaintext highlighter-rouge">X</code> or an <code class="language-plaintext highlighter-rouge">O</code> in them.</li>
      <li data-marker="*">Any return value is acceptable if a terminal board is provided as input.</li>
    </ul>
  </li>
  <li data-marker="*">The <code class="language-plaintext highlighter-rouge">result</code> function takes a <code class="language-plaintext highlighter-rouge">board</code> and an <code class="language-plaintext highlighter-rouge">action</code> as input, and should return a new board state, without modifying the original board.
    <ul>
      <li data-marker="*">If <code class="language-plaintext highlighter-rouge">action</code> is not a valid action for the board, your program should <a href="https://docs.python.org/3/tutorial/errors.html#raising-exceptions">raise an exception</a>.</li>
      <li data-marker="*">The returned board state should be the board that would result from taking the original input board, and letting the player whose turn it is make their move at the cell indicated by the input action.</li>
      <li data-marker="*">Importantly, the original board should be left unmodified: since Minimax will ultimately require considering many different board states during its computation. This means that simply updating a cell in <code class="language-plaintext highlighter-rouge">board</code> itself is not a correct implementation of the <code class="language-plaintext highlighter-rouge">result</code> function. You’ll likely want to make a <a href="https://docs.python.org/3/library/copy.html#copy.deepcopy">deep copy</a> of the board first before making any changes.</li>
    </ul>
  </li>
  <li data-marker="*">The <code class="language-plaintext highlighter-rouge">winner</code> function should accept a <code class="language-plaintext highlighter-rouge">board</code> as input, and return the winner of the board if there is one.
    <ul>
      <li data-marker="*">If the X player has won the game, your function should return <code class="language-plaintext highlighter-rouge">X</code>. If the O player has won the game, your function should return <code class="language-plaintext highlighter-rouge">O</code>.</li>
      <li data-marker="*">One can win the game with three of their moves in a row horizontally, vertically, or diagonally.</li>
      <li data-marker="*">You may assume that there will be at most one winner (that is, no board will ever have both players with three-in-a-row, since that would be an invalid board state).</li>
      <li data-marker="*">If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function should return <code class="language-plaintext highlighter-rouge">None</code>.</li>
    </ul>
  </li>
  <li data-marker="*">The <code class="language-plaintext highlighter-rouge">terminal</code> function should accept a <code class="language-plaintext highlighter-rouge">board</code> as input, and return a boolean value indicating whether the game is over.
    <ul>
      <li data-marker="*">If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function should return <code class="language-plaintext highlighter-rouge">True</code>.</li>
      <li data-marker="*">Otherwise, the function should return <code class="language-plaintext highlighter-rouge">False</code> if the game is still in progress.</li>
    </ul>
  </li>
  <li data-marker="*">The <code class="language-plaintext highlighter-rouge">utility</code> function should accept a terminal <code class="language-plaintext highlighter-rouge">board</code> as input and output the utility of the board.
    <ul>
      <li data-marker="*">If X has won the game, the utility is <code class="language-plaintext highlighter-rouge">1</code>. If O has won the game, the utility is <code class="language-plaintext highlighter-rouge">-1</code>. If the game has ended in a tie, the utility is <code class="language-plaintext highlighter-rouge">0</code>.</li>
      <li data-marker="*">You may assume <code class="language-plaintext highlighter-rouge">utility</code> will only be called on a <code class="language-plaintext highlighter-rouge">board</code> if <code class="language-plaintext highlighter-rouge">terminal(board)</code> is <code class="language-plaintext highlighter-rouge">True</code>.</li>
    </ul>
  </li>
  <li data-marker="*">The <code class="language-plaintext highlighter-rouge">minimax</code> function should take a <code class="language-plaintext highlighter-rouge">board</code> as input, and return the optimal move for the player to move on that board.
    <ul>
      <li data-marker="*">The move returned should be the optimal action <code class="language-plaintext highlighter-rouge">(i, j)</code> that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.</li>
      <li data-marker="*">If the <code class="language-plaintext highlighter-rouge">board</code> is a terminal board, the <code class="language-plaintext highlighter-rouge">minimax</code> function should return <code class="language-plaintext highlighter-rouge">None</code>.</li>
    </ul>
  </li>
</ul>

<p>For all functions that accept a <code class="language-plaintext highlighter-rouge">board</code> as input, you may assume that it is a valid board (namely, that it is a list that contains three rows, each with three values of either <code class="language-plaintext highlighter-rouge">X</code>, <code class="language-plaintext highlighter-rouge">O</code>, or <code class="language-plaintext highlighter-rouge">EMPTY</code>). You should not modify the function declarations (the order or number of arguments to each function) provided.</p>

<p>Once all functions are implemented correctly, you should be able to run <code class="language-plaintext highlighter-rouge">python runner.py</code> and play against your AI. And, since Tic-Tac-Toe is a tie given optimal play by both sides, you should never be able to beat the AI (though if you don’t play optimally as well, it may beat you!)</p>

<h2 id="hints">Hints</h2>

<ul>
  <li data-marker="*">If you’d like to test your functions in a different Python file, you can import them with lines like <code class="language-plaintext highlighter-rouge">from tictactoe import initial_state</code>.</li>
  <li data-marker="*">You’re welcome to add additional helper functions to <code class="language-plaintext highlighter-rouge">tictactoe.py</code>, provided that their names do not collide with function or variable names already in the module.</li>
  <li data-marker="*">Alpha-beta pruning is optional, but may make your AI run more efficiently!</li>
</ul>

</main>