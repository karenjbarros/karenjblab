# Codigo de Analise de Churn 

# Importando bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Carregando os dados (exemplo ficticio)
df = pd.read_csv("churn.csv")  # Substitua pelo seu dataset real

# Explorando os dados
print(df.head())  # Exibe as primeiras linhas do dataset
print(df.info())  # Mostra informações sobre os tipos de dados
print(df["Churn"].value_counts())  # Verifica o balanceamento da variável alvo

# Visualizando a distribuição de clientes que cancelaram vs. os que permaneceram
sns.countplot(data=df, x="Churn")
plt.title("Distribuição de Churn")
plt.show()

# Selecionando as variáveis para análise
X = df.drop(columns=["Churn", "CustomerID"])  # Remove a variável alvo e ID do cliente
y = df["Churn"].map({"No": 0, "Yes": 1})  # Converte "Yes"/"No" para 1/0

# Dividindo os dados em treino e teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Padronizando os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Criando e treinando um modelo de Machine Learning (Random Forest)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Fazendo previsões
y_pred = model.predict(X_test)

# Avaliando o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia do Modelo: {accuracy:.2f}")

# Relatório de Classificação
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))

# Matriz de Confusão
plt.figure(figsize=(5,4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d", cmap="Blues")
plt.xlabel("Previsto")
plt.ylabel("Real")
plt.title("Matriz de Confusão")
plt.show()

