{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "128f996a-7e6c-4b6f-9168-ee80edb1598b",
   "metadata": {},
   "source": [
    "# Imports"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4816c6a9-d0fc-42ee-a643-5f76b91797f5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5459691f-848f-4102-8891-46f2a16284c0",
   "metadata": {},
   "source": [
    "# Gerando números aleatórios"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6f726acb-9829-45fa-af1d-a1354a34a5df",
   "metadata": {},
   "outputs": [],
   "source": [
    "random_arr = np.random.random((3, 3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "aac00971-cf2e-4efb-808e-2cced11491b2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Matriz aleatória:\n",
      " [[0.19080529 0.95575568 0.87895634]\n",
      " [0.91113625 0.24628114 0.29381638]\n",
      " [0.06320251 0.17206094 0.86452103]]\n"
     ]
    }
   ],
   "source": [
    "print(\"Matriz aleatória:\\n\", random_arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "beb1410d-8527-4324-a889-365d10d98eba",
   "metadata": {},
   "source": [
    "# Produto escalar"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "29c223a7-0d70-4d26-9679-c3a10fe76521",
   "metadata": {},
   "source": [
    "## O que é?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d10b2a54-382b-4557-8fd9-fbfada29a7c9",
   "metadata": {},
   "source": [
    "O produto escalar (ou dot product) é uma operação matemática que combina dois vetores e resulta em um número escalar. Ele é amplamente utilizado em álgebra linear, computação gráfica e aprendizado de máquina.\n",
    "\n",
    "Definição Matemática\n",
    "Se tivermos dois vetores \n",
    "𝑎\n",
    "a e \n",
    "𝑏\n",
    "b de mesma dimensão:\n",
    "\n",
    "𝑎\n",
    "=\n",
    "[\n",
    "𝑎\n",
    "1\n",
    ",\n",
    "𝑎\n",
    "2\n",
    ",\n",
    "…\n",
    ",\n",
    "𝑎\n",
    "𝑛\n",
    "]\n",
    "a=[a \n",
    "1\n",
    "​\n",
    " ,a \n",
    "2\n",
    "​\n",
    " ,…,a \n",
    "n\n",
    "​\n",
    " ]\n",
    "𝑏\n",
    "=\n",
    "[\n",
    "𝑏\n",
    "1\n",
    ",\n",
    "𝑏\n",
    "2\n",
    ",\n",
    "…\n",
    ",\n",
    "𝑏\n",
    "𝑛\n",
    "]\n",
    "b=[b \n",
    "1\n",
    "​\n",
    " ,b \n",
    "2\n",
    "​\n",
    " ,…,b \n",
    "n\n",
    "​\n",
    " ]\n",
    "O produto escalar é calculado como:\n",
    "\n",
    "𝑎\n",
    "⋅\n",
    "𝑏\n",
    "=\n",
    "𝑎\n",
    "1\n",
    "𝑏\n",
    "1\n",
    "+\n",
    "𝑎\n",
    "2\n",
    "𝑏\n",
    "2\n",
    "+\n",
    "⋯\n",
    "+\n",
    "𝑎\n",
    "𝑛\n",
    "𝑏\n",
    "𝑛\n",
    "a⋅b=a \n",
    "1\n",
    "​\n",
    " b \n",
    "1\n",
    "​\n",
    " +a \n",
    "2\n",
    "​\n",
    " b \n",
    "2\n",
    "​\n",
    " +⋯+a \n",
    "n\n",
    "​\n",
    " b \n",
    "n\n",
    "​\n",
    " \n",
    "Ou, em notação de somatório:\n",
    "\n",
    "𝑎\n",
    "⋅\n",
    "𝑏\n",
    "=\n",
    "∑\n",
    "𝑖\n",
    "=\n",
    "1\n",
    "𝑛\n",
    "𝑎\n",
    "𝑖\n",
    "𝑏\n",
    "𝑖\n",
    "a⋅b= \n",
    "i=1\n",
    "∑\n",
    "n\n",
    "​\n",
    " a \n",
    "i\n",
    "​\n",
    " b \n",
    "i\n",
    "​\n",
    " \n",
    "Interpretação Geométrica\n",
    "O produto escalar também pode ser expresso em termos do ângulo \n",
    "𝜃\n",
    "θ entre os vetores:\n",
    "\n",
    "𝑎\n",
    "⋅\n",
    "𝑏\n",
    "=\n",
    "∣\n",
    "∣\n",
    "𝑎\n",
    "∣\n",
    "∣\n",
    "⋅\n",
    "∣\n",
    "∣\n",
    "𝑏\n",
    "∣\n",
    "∣\n",
    "⋅\n",
    "cos\n",
    "⁡\n",
    "(\n",
    "𝜃\n",
    ")\n",
    "a⋅b=∣∣a∣∣⋅∣∣b∣∣⋅cos(θ)\n",
    "Onde:\n",
    "\n",
    "∣\n",
    "∣\n",
    "𝑎\n",
    "∣\n",
    "∣\n",
    "∣∣a∣∣ e \n",
    "∣\n",
    "∣\n",
    "𝑏\n",
    "∣\n",
    "∣\n",
    "∣∣b∣∣ são as normas (módulos) dos vetores.\n",
    "cos\n",
    "⁡\n",
    "(\n",
    "𝜃\n",
    ")\n",
    "cos(θ) representa o cosseno do ângulo entre eles.\n",
    "Se o produto escalar for zero, significa que os vetores são ortogonais (perpendiculares)."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "771a7b46-859b-4b04-ad59-a2fdc7eb0c17",
   "metadata": {},
   "source": [
    "## Aplicações do Produto Escalar"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "748ae491-ede8-44bd-960e-1debb8c2ee4c",
   "metadata": {},
   "source": [
    "Cálculo de ângulo entre vetores (importante para aprendizado de máquina e visão computacional).\n",
    "Projeção de um vetor sobre outro (útil em física e computação gráfica).\n",
    "Verificação de ortogonalidade (se o produto escalar for 0, os vetores são perpendiculares).\n",
    "Redução dimensional em aprendizado de máquina (como em PCA – Principal Component Analysis)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9bde9bdc-96d6-4ea3-80b8-5ff12401d428",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr1 = np.array([1, 2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4a553a45-65b7-4795-8fe8-a0faa0f4b54e",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr2 = np.array([3, 4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d73f1217-abaf-4b83-8d91-714d8f230d93",
   "metadata": {},
   "outputs": [],
   "source": [
    "dot_product = np.dot(arr1, arr2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "56dedcd7-66f7-42cc-b1ad-5f2f5454303f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Produto escalar: 11\n"
     ]
    }
   ],
   "source": [
    "print(\"Produto escalar:\", dot_product)"
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
