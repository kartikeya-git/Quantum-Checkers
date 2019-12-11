import unreal_engine as ue

from qiskit import execute, QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.quantum_info.operators import Operator
from qiskit.quantum_info import process_fidelity
from qiskit.providers.aer import QasmSimulator
from qiskit.providers.aer.noise import NoiseModel, errors

from qiskit.tools.visualization import plot_histogram

from qiskit import Aer, execute
import numpy as np
from qiskit.extensions.simulator import Snapshot
from qiskit.extensions.simulator.snapshot import snapshot

simulator = Aer.get_backend('qasm_simulator')
# Define the simulation method
backend_opts_mps = {"method":"matrix_product_state"}  

sqrt2i = 1/(np.sqrt(2))

iswap_op = Operator([[1, 0, 0, 0],
                     [0, 0, 1j, 0],
                     [0, 1j, 0, 0],
                     [0, 0, 0, 1]])

sqrt_iswap_op = Operator([[1, 0, 0, 0],
                     [0, sqrt2i, sqrt2i*1j, 0],
                     [0, sqrt2i*1j, sqrt2i, 0],
                     [0, 0, 0, 1]])

sqrt_iswap_adj_op = Operator([[1, 0, 0, 0],
                     [0, sqrt2i, -sqrt2i*1j, 0],
                     [0, -sqrt2i*1j, sqrt2i, 0],
                     [0, 0, 0, 1]])


def full_measure(num_of_shots = 10000):
    
    circ.measure(qr, cr)

    result = execute(circ, simulator, backend_options=backend_opts_mps, shots = num_of_shots).result()
    counts = result.get_counts(circ)
    return counts


def get_prob(n_shots=90):
    counts = full_measure(num_of_shots=n_shots)
    L = []
    for bit, shots in counts.items():
        x = [bit, shots]
        L.append(x)

    P = []
    for qubit in range(32):
        s = 0
        for i in L:
            bit, shots = i[0], i[1]
            bit_num = int(bit[-(qubit + 1)])
            if (bit_num == 1):
                s += shots
        P.append(str(s / n_shots))
    return P


def measurement(qubit):
    circ.measure(qr[qubit], cr[qubit])

    result = execute(circ, simulator, backend_options=backend_opts_mps, shots = 1).result()
    es_counts = result.get_counts(circ)

    state = list(es_counts.keys())[0]
    bit_num = int(state[-(qubit + 1)])
    circ.reset(qr[qubit])
    if bit_num == 1:
        circ.x(qr[qubit])

    ent = entanglement_dict[str(qubit)]
    for i in ent:
        bn = int(state[-(int(i) + 1)])
        circ.reset(qr[int(i)])
        if bn:
            circ.x(qr[int(i)])

    return bit_num


def standard_move(s,t):
    circ.unitary(iswap_op, [s, t], label='iswap')


def quantum_move(s, t):
    circ.unitary(sqrt_iswap_op, [s, t], label='sqrt_iswap')

    source = entanglement_dict[str(s)]
    if t not in source:
        entanglement_dict[str(s)].append(t)
    target = entanglement_dict[str(t)]
    if s not in target:
        entanglement_dict[str(t)].append(s)
    merged = list(set(entanglement_dict[str(s)]) | set(entanglement_dict[str(t)]))

    entanglement_dict[str(s)] = merged
    entanglement_dict[str(t)] = merged
    # return entanglement_dict'''



num_qubits = 32
qr = QuantumRegister(num_qubits)
cr = ClassicalRegister(num_qubits)
circ = QuantumCircuit(qr, cr)


list_with_keys = [str(i) for i in range(num_qubits)]
list_with_values = [[] for i in range(num_qubits)]
entanglement_dict = dict(zip(list_with_keys, list_with_values))


for i in range(12):
    circ.x(qr[i])
for i in range(20, 32):
    circ.x(qr[i])


class QBoard:

    def begin_play(self):
        self.actor = self.uobject.get_owner()

    def normal_move(self):

        standard_move(int(self.actor.Source), int(self.actor.Target))

    def quantumm_move(self):

        quantum_move(self.actor.Source, self.actor.Target)

    def get_probability(self):
        return get_prob()#n_shots=self.actor.Shots)

    def measure(self):
        return measurement(self.actor.Measure)

    def reset_qubit(self):
        qubit = self.actor.ResetQubit
        circ.reset(qr[qubit])
        '''ent = entanglement_dict[str(qubit)]
        for j in ent:
            bn = int(state[-(int(j) + 1)])
            circ.reset(qr[int(j)])
            if bn:
                circ.x(qr[int(j)])'''

    def reset_qubit1(self):
        circ.reset(qr[self.actor.ResetQubit])
        circ.x(qr[self.actor.ResetQubit])



        