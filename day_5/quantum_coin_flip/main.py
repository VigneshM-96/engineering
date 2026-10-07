from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1, 1) # create the qubit and classical bit 

#apply hadamard gate
qc.h(0)

#qubit measure (from qubit 0 to classical bit 0)
qc.measure(0, 0)

#diagram
print("---Quantum Coin Flipper Diagram---")
print(qc.draw(output="text"))

#measure the qubit multiple times
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
results = job.result()

#record the counts
counts = results.get_counts()

print("---Simulation Results---")
print(f"Recorded Outcomes : (outof 1000 coin flips) : {counts}")
