# QuantumCheckers
 Quantum Checkers is a game of Checkers demonstrating effects of Quantum Mechanical phenomenon.
 
## Rules

The goal is to eliminate all your opponent's pieces. But now you have an advantage of making a quantum move, due to which you can split your piece with equal probabilities on the board. You or your opponent can force a measurement on the piece during an attempted capture, revealing it's position. Each square is a qubit in the IBMQ Qiskit simulator.  Get ready to create Schrodinger's cat like pieces, both Alive and Dead.

## Backend

The game runs on Unreal Engine 4 using Qiskit-Python as a tool for generating quantum effects. The UnrealEnginePython plugin is used to help Unreal Engine communicate with the Python program. The python program creates a 32 qubit circuit, one qubit for each square. With each move, a corresponding gate is applied to the respective qubits. A measurement takes pplace collapsing the state of the all associated qubits, when trying to move to a square which is in some kind of superposition.

### An embedded version of python with Qiskit and Numpy is needed to play this.

The final build should already include an embedded python. In case, it is not present, an embedded version of python, with the folder containing all the modules, must be extracted in the following location: <GameFolder>\QuantumCheckers\Binaries\

The Scripts folder should also be copied in the following location (if not already present): <GameFolder>\QuantumCheckers\Content\
 
 ### The game can also be directly played from inside Unreal Engine 4.22 (higher versions not supported by UnrealEnginePython plugin)


## Why Checkers?
Quantum mechanical phenomenon are not intuitive, even for the people who understand it's math, since we do not experience quantum effects in our daily lives on a macroscopic level. We do however, understand how to ride a bicycle, balancing and tilting it, without even knowing the math. Video games provide a platform for building intuition about stuff that we do not experience in our daily lives. Simple games like tic-tac-toe, chess, and checkers that require strategy, can help explore the weird world of quantum mechanics while enjoying the game.

 
