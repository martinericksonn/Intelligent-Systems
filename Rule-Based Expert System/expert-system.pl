go :-
    write('----------------------------------------------------------------------\n'),
    write('An expert system to analyize user''s possible disorder based on feedback \n'),
    write('----------------------------------------------------------------------\n'),
    write('What is the patient''s name? '),
    read(Patient),get_single_char(Code),
    hypothesis(Patient,Disease),
    write('----------------------------------------------------------------------\n'),
    write('----------------------------------------------------------------------\n'),
    write_list([Patient,', probably has ',Disease,'.']),nl,
    write('----------------------------------------------------------------------\n'),
    write('----------------------------------------------------------------------\n').
    
    go :-
    write('----------------------------------------------------------------------\n'),
    write('----------------------------------------------------------------------\n'),
    write('Sorry, I don''t seem to be able to'),nl,
    write('diagnose the disorder.'),nl,
    write('----------------------------------------------------------------------\n'),
    write('----------------------------------------------------------------------\n').

    symptom(Patient,worrying_social_situations) :- 
    verify(Patient," Worrying about social situations (y/n) ?").
    symptom(Patient,worrying_embarrassing_social_situations) :- 
    verify(Patient," worrying about embarrassing yourself in a social situation (y/n) ? ").
    symptom(Patient,avoiding_social_situations) :- 
    verify(Patient," Avoiding socialsituations (y/n) ?").
    symptom(Patient,conscious_actions) :- 
    verify(Patient," Conscious of your actions when in social settings (y/n) ? ").
    symptom(Patient,constantly_check) :- 
    verify(Patient," Do you experience the need to constantly check on something (y/n) ? ").
    symptom(Patient,intrusive_thoughts) :- 
    verify(Patient," Do you experience intrusive thoughts that are aggressive\n such as but not limited to porn (y/n) ? ").
    symptom(Patient,organise_items) :- 
    verify(Patient," Do you feel the need to organise items in a certain way (y/n) ?").
    symptom(Patient,repetitive_behaviours) :- 
    verify(Patient," Do you find yourself repeating words, counting or doing other\n repetitive behaviours when you are feeling anxious? (y/n) ? ").
    symptom(Patient,difficulty_concentrating) :- 
    verify(Patient," Having difficulty concentrating? (y/n) ? ").
    symptom(Patient,felt_numb ) :- 
    verify(Patient," Felt numb or detached from people, activities, or your surroundings?(y/n) ? ").
    symptom(Patient, stressful_experience) :- 
    verify(Patient," Feeling very upset when something reminded you of a stressful\n experience from the past? (y/n) ? ").
    symptom(Patient,nightmares) :- 
    verify(Patient," Had nightmares about the event/s or thought about the event/s\n when you did not want to? (y/n) ? ").
    symptom(Patient,irritability) :- 
    verify(Patient," Do you have frequent feelings of irritability and aggressiveness (y/n) ? ").
    symptom(Patient,emptiness) :- 
    verify(Patient," Have you felt chronic emptiness or loneliness (y/n) ? ").
    symptom(Patient,detachment) :- 
    verify(Patient," Have you experienced a pattern of detachment\n from social relationships (y/n) ? ").
    symptom(Patient,indifferent) :- 
    verify(Patient," Do you often feel indifferent to praise or criticisms from others? (y/n) ? ").
    symptom(Patient,reluctant) :- 
    verify(Patient," Are you reluctant to take personal risks or engage in new activities (y/n) ? ").
    symptom(Patient,self_doubt_overconfidence) :- 
    verify(Patient," My self-confidence ranges from GREAT self-doubt to\n EQUALLY GREAT overconfidence. (y/n) ? ").
    symptom(Patient,mentally_dul) :- 
    verify(Patient," Sometimes I am mentally dull and at other times I think VERY creatively. (y/n) ? ").
    symptom(Patient,optimism_pessimism) :- 
    verify(Patient," At some times I have GREAT optimism and at other times\n EQUALLY GREAT pessimism.(y/n) ? ").
    symptom(Patient,tearfulness) :- 
    verify(Patient," Some of the time I show MUCH tearfulness and crying and at\n other times I laugh and joke EXCESSIVELY (y/n) ? ").
    symptom(Patient,thoughts_hurting_yourself) :- 
    verify(Patient," Thoughts that you would be better off dead, or of hurting yourself (y/n) ? ").
    symptom(Patient,feeling_tired) :- 
    verify(Patient," Feeling tired or having little energy  (y/n) ? ").
    symptom(Patient,little_interest_in_doing_things) :- 
    verify(Patient," Little interest or pleasure in doing things (y/n) ? ").
    symptom(Patient,poor_appetite) :- 
    verify(Patient," Poor appetite or overeating (y/n) ? ").
    
    ask(Patient,Question) :-
        write('----------------------------------------------------------------------\n'), write(Question),
        read(N),
        ( (N == yes ; N == y)
          ->
           assert(yes(Question)) ;  
           assert(no(Question)), fail).
        
    :- dynamic yes/1,no/1.		
        
    verify(P,S) :-
       (yes(S) -> true ;
        (no(S) -> fail ;
         ask(P,S))).
         
    undo :- retract(yes(_)),fail. 
    undo :- retract(no(_)),fail.
    undo.
    
    
    hypothesis(Patient,post_traumatic_stress_disorder) :-
    symptom(Patient,felt_numb),
    symptom(Patient,difficulty_concentrating),
    symptom(Patient,nightmares),
    symptom(Patient,stressful_experience).

    hypothesis(Patient,depression) :-
    symptom(Patient,felt_numb),
    symptom(Patient,emptiness),
    symptom(Patient,thoughts_hurting_yourself),
    symptom(Patient,little_interest_in_doing_things),
    symptom(Patient,poor_appetite).

    hypothesis(Patient,social_anxiety_disorder) :-
    symptom(Patient,avoiding_social_situations),
    symptom(Patient,worrying_social_situations),
    symptom(Patient,worrying_embarrassing_social_situations),
    symptom(Patient,conscious_actions).

    hypothesis(Patient,obsessive_compulsive_disorder) :-
    symptom(Patient,organise_items),
    symptom(Patient,constantly_check),
    symptom(Patient,intrusive_thoughts),
    symptom(Patient,repetitive_behaviours).
    
    hypothesis(Patient,bipolar_disorder) :-
    symptom(Patient,irritability),
    symptom(Patient,self_doubt_overconfidence),
    symptom(Patient,mentally_dul),
    symptom(Patient,tearfulness),
    symptom(Patient,optimism_pessimism).


    hypothesis_check:-
        write('----------------------------------------------------------------------\n'),
        write_hypothesis(Patient,X),
        write('----------------------------------------------------------------------\n').


    write_hypothesis(Patient,post_traumatic_stress_disorder):-
        write('Post Trraumatic Stress Disorder\n'),
        write('Post-traumatic stress disorder PTSD is a mental health condition that''s triggered by a terrifying event '),nl,
        write('either experiencing it or witnessing it. Symptoms may include flashbacks, nightmares and severe anxiety,\nas well as uncontrollable thoughts about the event'),nl.
      
    
    write_hypothesis(Patient,depression):-
        write('Depression\n'),
        write('a common and serious medical illness that negatively affects how you feel, the way you think and how you act\n'),nl,
        write('Fortunately, it is also treatable. Depression causes feelings of sadness and/or a loss of interest in activities you once enjoyed.\n'),nl,
        write('It can lead to a variety of emotional and physical problems and can decrease your ability to function at work and at home.\n'),nl.
       
    
    write_hypothesis(Patient,social_anxiety_disorder):-
        write('Social Anxiety Disorder\n'),
        write('A mental health condition. It is an intense, persistent fear of being watched and judged by others\n'),nl,
        write('This fear can affect work, school, and your other day-to-day activities. It can even make it hard to make and keep friends.\n'),nl.

    write_hypothesis(Patient,obsessive_compulsive_disorder):-
        write('Obsessive Compulsive Disorder\n'),
        write('Features a pattern of unwanted thoughts and fears (obsessions) that lead you to do repetitive behaviors\n'),nl,
        write('These obsessions and compulsions interfere with daily activities and cause significant distress.\n'),nl.
        
    write_hypothesis(Patient,bipolar_disorder):-
        write('Bipolar Disorder\n'),
        write('is a brain and behavior disorder characterized by severe shifts in a person''s mood and energy making \n'),nl,
        write('it difficult for the person to function.The condition typically starts in late adolescence or early adulthood,\n'),nl,
        write('The condition typically starts in late adolescence or early adulthood although it can show up in children and in older adults\n'),nl.
    

    

    write_list([]).
    write_list([Term| Terms]) :-
    write(Term),
    write_list(Terms).
    
    response(Reply) :-
    get_single_char(Code),
    put_code(Code), nl,
    char_code(Reply, Code).
    