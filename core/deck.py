import random
suite=["H","C","D","S"]
J=Q=K=[10]
rank=["2","3","4","5","6","7","8","9","10","J","Q", "K","A"]
in_place=[]     
     
      
       
def build_standard_deck() -> list[dict]:
     
    for i in suite:
        for j in rank:
            in_place.append({j:i})      
        
        return in_place    
build_standard_deck()
# def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
   
    
    
       
