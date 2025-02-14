{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "182b3e09-001d-49a5-8d9d-d8968c54f83b",
   "metadata": {},
   "source": [
    "# Imports"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8924bb43-2246-4da4-bbff-59ea9fe9aa96",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6a59c5cc-d144-46d0-aa48-aadf6b40d14b",
   "metadata": {},
   "source": [
    "# Estatísticas básicas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "540e1df8-bbcf-4833-b920-9e884b0c24d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr = np.array([1, 2, 3, 4, 5])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f7222804-16fa-424d-9d6d-ca2214439ec6",
   "metadata": {},
   "source": [
    "## Média"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "37a042d2-4e2f-4ce1-812d-d2923efd22c6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Média: 3.0\n"
     ]
    }
   ],
   "source": [
    "print(\"Média:\", np.mean(arr))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1bee0a31-16c4-4cc9-9a3c-7492b0a8c55f",
   "metadata": {},
   "source": [
    "## Desvio Padrão"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "25c70e6f-65fa-4cdc-9e23-5a4c89dee7c0",
   "metadata": {},
   "source": [
    "O desvio padrão é uma medida estatística que indica o grau de dispersão ou variação de um conjunto de dados em relação à sua média. Em outras palavras, ele mostra o quanto os valores de um conjunto estão espalhados em torno da média.\n",
    "\n",
    "Interpretação\n",
    "Desvio padrão baixo: Os valores estão mais próximos da média (pouca variação).\n",
    "Desvio padrão alto: Os valores estão mais espalhados (muita variação).\n",
    "\n",
    "#### Exemplo:\n",
    "\n",
    "Conjunto 1: [10, 12, 11, 9, 10] → Baixo desvio padrão (valores próximos).\n",
    "Conjunto 2: [5, 20, 3, 30, 2] → Alto desvio padrão (valores muito dispersos).\n",
    "\n",
    "Se o desvio padrão for maior que a média ou um valor próximo dela, os dados têm alta variação.\n",
    "\n",
    "#### Coeficiente de Variação (CV)\n",
    "\n",
    "O Coeficiente de Variação (CV) é uma forma padronizada de comparar desvios padrão entre conjuntos com escalas diferentes.\n",
    "\n",
    "#### Avaliação de Resultados\n",
    "\n",
    "CV<10% → Baixa dispersão\n",
    "\n",
    "10%≤CV≤20% → Dispersão moderada\n",
    "\n",
    "CV>20% → Alta dispersão"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3dd6c38c-ef95-4d9a-b4e0-76c355de1020",
   "metadata": {},
   "source": [
    "### Exemplo de Baixo Desvio Padrão"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "731e8785-6256-4e78-bbfd-35e84542dfed",
   "metadata": {},
   "outputs": [],
   "source": [
    "cj1 = [10, 12, 11, 9, 10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "31b64c8d-e62f-48bc-9cb0-023864cdac5e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Média cj1: 10.4\n"
     ]
    }
   ],
   "source": [
    "print(\"Média cj1:\", np.mean(cj1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f4d0acb9-1e49-4c4e-9740-8fa4670477b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Desvio padrão cj1: 1.0198039027185568\n"
     ]
    }
   ],
   "source": [
    "print(\"Desvio padrão cj1:\", np.std(cj1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "2711d335-818e-4af8-a01a-eb81a222a3bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "CVcj1 = np.std(cj1)/np.mean(cj1)*100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a1eac439-46e6-4189-b4be-23193780aa0d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Coeficiente de Variação (CV) cj1: 9.805806756909199\n"
     ]
    }
   ],
   "source": [
    "print(\"Coeficiente de Variação (CV) cj1:\", CVcj1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b2aae4b1-6d45-465b-ab58-907df3a5f4c4",
   "metadata": {},
   "source": [
    "### Exemplo de Alto Desvio Padrão"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "be3872e7-8078-42a3-9bfc-764032511b12",
   "metadata": {},
   "outputs": [],
   "source": [
    "cj2 = [5, 20, 3, 30, 2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f7c42e03-e2bc-4c8c-b86b-924c890cc921",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Média cj2: 12.0\n"
     ]
    }
   ],
   "source": [
    "print(\"Média cj2:\", np.mean(cj2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "cff49c4d-c22f-4d11-a145-84cc78e0545b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Desvio padrão cj2: 11.117553687749837\n"
     ]
    }
   ],
   "source": [
    "print(\"Desvio padrão cj2:\", np.std(cj2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "cb2d2b1e-1e0d-4f65-b132-4dc5a8b3caff",
   "metadata": {},
   "outputs": [],
   "source": [
    "CVcj2 = np.std(cj2)/np.mean(cj2)*100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "4bcf965f-7274-4021-8034-d0df097de593",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Coeficiente de Variação (CV) cj2: 92.64628073124864\n"
     ]
    }
   ],
   "source": [
    "print(\"Coeficiente de Variação (CV) cj2:\", CVcj2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ec624674-a53b-4628-8d16-0a7b50aed429",
   "metadata": {},
   "source": [
    "### Resumo Prático\n",
    "\n",
    "**Baixo desvio padrão quando:**\n",
    "\n",
    "- 𝜎 é pequeno em relação à média (μ)\n",
    "\n",
    "- A maioria dos dados está concentrada perto da média\n",
    "\n",
    "- O coeficiente de variação CV é menor que 10%\n",
    "\n",
    "**Alto desvio padrão quando:**\n",
    "\n",
    "- 𝜎 é grande comparado à média\n",
    "\n",
    "- Os dados estão muito dispersos\n",
    "\n",
    "- O coeficiente de variação CV ultrapassa 20%"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "8152a51b-90a4-41e1-9893-fbe846a3d460",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Desvio padrão: 1.4142135623730951\n"
     ]
    }
   ],
   "source": [
    "print(\"Desvio padrão:\", np.std(arr))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0bfd0056-1669-49d2-85f9-994abc895b73",
   "metadata": {},
   "source": [
    "# Algebra Linear: Produto de matrizes"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "49268c63-74e2-42f5-82d7-178b1746ea7d",
   "metadata": {},
   "source": [
    "Dadas duas matrizes:\n",
    "\n",
    "𝐴 de dimensão 𝑚 × 𝑛 (m linhas e n colunas)\n",
    "\n",
    "\n",
    "B de dimensão 𝑛 × 𝑝 (n linhas e p colunas)\n",
    "\n",
    "O produto 𝐶 = 𝐴 ⋅ 𝐵 só é possível se o número de colunas de 𝐴 for igual ao número de linhas de 𝐵 .\n",
    "\n",
    "Dimensão do resultado: A matriz 𝐶 terá 𝑚 linhas e 𝑝 colunas.\n",
    "\n",
    "(𝑚×𝑛)⋅(𝑛×𝑝)=(𝑚×𝑝)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "9bf64af0-39c3-49e9-b792-c97c67c47776",
   "metadata": {},
   "outputs": [],
   "source": [
    "A = np.array([[1, 2], [3, 4]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "b6c02629-0f50-4c59-ae4a-ef026cd98e29",
   "metadata": {},
   "outputs": [],
   "source": [
    "B = np.array([[5, 6], [7, 8]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5859540a-afb7-4085-bd4e-40536f2325e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "product = np.dot(A, B)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "3c1da37e-a728-4d61-b76c-29c29031aeb9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Produto de matrizes:\n",
      " [[19 22]\n",
      " [43 50]]\n"
     ]
    }
   ],
   "source": [
    "print(\"Produto de matrizes:\\n\", product)"
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
