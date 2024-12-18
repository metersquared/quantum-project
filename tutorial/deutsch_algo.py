from qrisp import QuantumVariable, h, cx, x, barrier, measure


# Create oracle function
def oracle_function(qv: QuantumVariable, type="unbalanced0"):
    match type:
        case "unbalanced0":
            return qv
        case "unbalanced1":
            x(qv[1])
            return qv
        case "balanced":
            cx(qv[0], qv[1])
            return qv


## DEUTSCH ALGORITHM ##
# Initialize the state to 01
qv = QuantumVariable(2)
x(qv[1])
barrier(qv)

# Apply Hadamard gate to both
h(qv)
barrier(qv)

# Apply Oracle function
oracle_function(qv, "unbalanced0")
barrier(qv)

# Apply Hadamard on first qubit
h(qv[0])

qv.reduce(qv[1])

# Print measurment
print(qv.get_measurement(shots=1))


## DEUTSCH-JOSZA ALGORITHM ##
# Initialize the state to 01
qv = QuantumVariable(10)
x(qv[1])
barrier(qv)

# Apply Hadamard gate to both
h(qv)
barrier(qv)

# Apply Oracle function
oracle_function(qv, "balanced")
barrier(qv)

# Apply Hadamard on first qubit
h(qv[0])
