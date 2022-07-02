import torch
import torch.nn as nn

X = torch.Tensor([[0, 0], [0, 1], [1, 0], [1, 1]])  # 입력 데이터
Y = torch.Tensor([[0], [0], [0], [1]])  # target 값 (= 정답값) for AND gate
Y = torch.Tensor([[0], [1], [1], [0]])  # target 값 (= 정답값) for OR gate

model = nn.Sequential(
    nn.Linear(2, 500),
    nn.ReLU(),
    nn.Linear(500, 1),
    nn.Sigmoid(),
)
loss_func = torch.nn.BCELoss()  # binary classification을 위해 BCELoss 사용

num_epochs = 2000  # 반복 횟수 지정
optimizer = torch.optim.SGD(model.parameters(), lr=0.2)
# 다양한 optimizer 중에서 제일 simple한
# SGD (Stochastic Gradient Descent) optimizer 사용

for epoch in range(num_epochs + 1):
    prediction = model(X)  # 순전파 과정
    loss = loss_func(prediction, Y)  # 손실 함수 계산

    optimizer.zero_grad()  # 기울기값 초기화
    loss.backward()  # 기울기값 계산
    optimizer.step()  # 가중치 업데이트

    if epoch % 100 == 0:  # 특정 조건 만족할 때마다 현재 진행 상태 표시
        print(f"Epoch: {epoch:4d}  loss = {loss.item():8.5f}")
        print("prediction =", prediction.detach().squeeze().numpy())
        print()

prediction = model(X)  # 실수/확률 형태의 예측 출력값
pred_final = (prediction > 0.5).float()  # (0 또는 1) 형태의 예측 출력값
accuracy = (pred_final == Y).float().mean()  # 예측 출력값과 정답값 비교
print("prediction =", prediction.detach().squeeze().numpy())
print("pred_final =", pred_final.detach().squeeze().numpy())
print("target     =", Y.squeeze().numpy())  # 정답값
print("accuracy   =", accuracy.item() * 100, "%")
