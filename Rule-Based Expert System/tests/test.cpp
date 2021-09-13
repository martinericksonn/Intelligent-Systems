    int isWellOrdered(int number){
        int isOrdered = 1, prev = -1,  type = -1;
        
        while(number != 0){
            if(type ==-1){

                if(prev ==-1) {
                    prev = number % 10;
                    number = number/10;
                    continue;
                }

                if(prev == number % 10){  
                    isOrdered = 0;
                    break;
                }
                
                if(prev > number % 10){ 
                    type = 1;
                    prev = number % 10;
                    number = number/10;
                    continue;
                }

                prev = number % 10;
                number = number / 10;
            }
            
            else {  
                if(prev == number % 10){  
                    isOrdered = 0;
                    break;
                }
                
                if(prev < number % 10){          
                    isOrdered = 0;
                    break;
                }
                
                prev = number % 10;
                number = number / 10;
            }
        }
        return isOrdered;
    }   