import pandas as pd

def main():
    # 1. 학생 성적 예시 데이터 생성
    data = {
        "이름": ["민수", "지우", "서연", "도윤", "하은"],
        "중간고사": [85, 92, 78, 95, 88],
        "기말고사": [90, 88, 82, 98, 94]
    }
    
    # 2. 판다스 표(DataFrame)로 변환 및 평균 계산
    df = pd.DataFrame(data)
    df["평균점수"] = (df["중간고사"] + df["기말고사"]) / 2
    
    # 3. 결과 화면 출력
    print("=== 학생 성적 표 ===")
    print(df)
    
    print("\n=== 전체 통계 ===")
    print(f"전체 평균 점수: {df['평균점수'].mean():.2f}점")
    print(f"최고 득점자: {df.loc[df['평균점수'].idxmax(), '이름']}")

if __name__ == "__main__":
    main()
