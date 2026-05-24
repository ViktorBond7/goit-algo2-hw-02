def find_min_max(arr):

    if len(arr) == 1:
        return arr[0], arr[0]
    
    if len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0]) 
  
    mid = len(arr) // 2

    left_arr = arr[:mid]
    right_arr = arr[mid:]
    
    left_min, left_max = find_min_max(left_arr)
    right_min, right_max = find_min_max(right_arr)
     
    # step compare the minimums and maximums from both halves
    final_min = left_min if left_min < right_min else right_min
    final_max = left_max if left_max > right_max else right_max
    
    return final_min, final_max


if __name__ == "__main__":
   
    numbers = [1, 3, 5, 9, 7, 6]
    min_value, max_value = find_min_max(numbers)    
    print(f"Min: {min_value}, Max: {max_value}")