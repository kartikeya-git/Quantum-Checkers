# QuantumCheckers
 Quantum Checkers is a game of Checkers demonstrating effects of Quantum Mechanical phenomenon like entanglement, interference and superposition. It is also possible to get a Schrodinger's Cat like situation in the game. The game just doesn't use "randomness" as a special effect(which isn't completely quantum), it is a quantum circuit behaving like a game of checkers.
 ***NOTE: This game has been submitted for the IBM Quantum Awards 2019.***
 
 ***Gameplay video: www.youtube.com/watch?v=FklcCPCSuSw***
 
 ***Use the Release tab to download and run the game. Download and run the QuantumCheckers_setup.exe file. Follow the install instructions. After the setup is complete, you can run the game from QuantumCheckers.exe.***

***Direct link to Release: https://github.com/VvenomSsnake/Quantum-Checkers/releases/download/1.0/QuantumCheckers_setup.exe***

## Rules

The goal is to eliminate all your opponent's pieces. Now you have an advantage of making a quantum move, which move your piece with 50% probability. A measurement can be forced on a piece during an attempted capture, or a standard move, revealing it's position. Each square is a qubit in the IBMQ Qiskit simulator. You can also create Schrodinger's cat like pieces, both Alive and Dead.

## Why Checkers?

Quantum mechanics is not intuitive, even for the people who understand it's math, since we do not experience quantum effects in our daily lives on a macroscopic level. We do however, understand and learn how to ride a bicycle, balancing and tilting it, without even knowing the math. Video games provide a platform for building intuition about stuff that we do not experience in our daily lives. Simple games like tic-tac-toe, chess, and checkers that require strategy, can help explore the weird world of quantum mechanics while enjoying the game.

## Backend

The game runs on Unreal Engine 4 using Qiskit-Python as a tool for generating quantum effects. The UnrealEnginePython plugin is used to help Unreal Engine communicate with the Python program. The python program creates a 32 qubit circuit, one qubit for each square. With each move, a corresponding gate is applied to the respective qubits. A measurement takes pplace collapsing the state of the all associated qubits, when trying to move to a square which is in some kind of superposition.
### An embedded version of python with Qiskit and Numpy is needed to play this, all are included in the release.
### The game can also be directly played from inside Unreal Engine 4.22 (higher versions not supported by UnrealEnginePython plugin)

![Screenshot1](https://github.com/VvenomSsnake/Quantum-Checkers/blob/master/Screenshots/5.png)
![Screenshot2](https://github.com/VvenomSsnake/Quantum-Checkers/blob/master/Screenshots/6.png)

## Operations in the circuit

Each square represents a qubit. The states |0> and |1> correspond to an empty square and a piece being on the square respectively. Here's an example with two qubits.
![CIrcuit Initialization](https://github.com/VvenomSsnake/Quantum-Checkers/blob/master/Screenshots/__init.png)

A unitary is applied in each move, with some classical logic happening in the UnrealEngine separate from the circuit during the captures.
![Unitary](https://github.com/VvenomSsnake/Quantum-Checkers/blob/master/Screenshots/Unitary.png)

When you make a normal move, an iswap gate is applied to the corresponding qubits.
![Regular Move](https://github.com/VvenomSsnake/Quantum-Checkers/blob/master/Screenshots/standardmove.png)

When you make a quantum move, the square root of iswap is applied. The goal is to have a gate that would create a superposition between the |10> and |01> states. The iswap has been chosen for demonstrating interference.
![Quantum Move](https://github.com/VvenomSsnake/Quantum-Checkers/blob/master/Screenshots/qmove.png)

A capture implements a three piece measurement decision tree in the UnrealEngine, and resets the qubit corresponding to the captured piece back to 0, if it measured to be there. This might create a half dead half alive piece. 
