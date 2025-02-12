{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d099346b-7f77-449c-8354-6cbca35e0032",
   "metadata": {},
   "source": [
    "# Imports"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1c33e43c-feb1-47f0-83f0-4bb3af48e4eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5cd5c2c0-0209-448f-8823-265f465c90fe",
   "metadata": {},
   "source": [
    "# Reshaping de array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "17cf9fbd-2dd5-4df5-9474-9458ab431d9e",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr = np.array([1, 2, 3, 4, 5, 6])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3d81caea-b230-49e5-b7fa-0b26f2cad595",
   "metadata": {},
   "outputs": [],
   "source": [
    "reshaped = arr.reshape(2, 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d124b3b8-2313-41b8-b14f-db82e35122da",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array reshaped:\n",
      " [[1 2 3]\n",
      " [4 5 6]]\n"
     ]
    }
   ],
   "source": [
    "print(\"Array reshaped:\\n\", reshaped)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "81535539-1dbf-4421-867b-367db1bc2c0e",
   "metadata": {},
   "source": [
    "# Concatenando arrays"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "30ae1008-292f-44df-a3bf-228b488d822f",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr1 = np.array([1, 2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7c42bf0d-7ed9-4573-a642-17356abbe4f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr2 = np.array([3, 4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "1d932719-08e3-4054-91a9-d0d942fbbe1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "concatenated = np.concatenate((arr1, arr2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "19fb4454-9568-41a0-806e-081f040b0eed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array concatenado: [1 2 3 4]\n"
     ]
    }
   ],
   "source": [
    "print(\"Array concatenado:\", concatenated)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
