from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

#creating single single qubit circuit (1 qubit, 1 classical bit)
qc = QuantumCircuit(1, 1)

qc.x(0) #apply x gate to flip |0> to |1>

qc.h(0) #apply h gate (creates 50/50 superposition)

qc.measure(0, 0) # maps qubit 0 to classical bit 0

print("---Circuit Diagram Blueprint---")
print(qc.draw(output="text"))

simulator = AerSimulator()
job = simulator.run(qc, shots=1024)
results = job.result()
counts = results.get_counts()

print("Simulation results--------\n")
print(f"Measurement counts (out of 1024 runs) : {counts}")
print("\nInterpretation:")
print("Because the H gate put the qubit into a 50/50 superposition.")
