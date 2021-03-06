go :-
    write('What is the patient''s name? '),
    read(Patient),get_single_char(Code),
    hypothesis(Patient,Disease),
    write_list([Patient,',You probably have ',Disease,'.']),nl.
    
    go :-
    write('Sorry, I don''t seem to be able to'),nl,
    write('diagnose the disorder.'),nl.
    
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
    verify(Patient," Do you experience intrusive thoughts that are aggressive such as but not limited to porn (y/n) ? ").
    symptom(Patient,organise_items) :- 
    verify(Patient," Do you feel the need to organise items in a certain way (y/n) ?").
    symptom(Patient,repetitive_behaviours) :- 
    verify(Patient," Do you find yourself repeating words, counting or doing other repetitive behaviours when you are feeling anxious? (y/n) ? ").
    symptom(Patient,difficulty_concentrating) :- 
    verify(Patient," Having difficulty concentrating? (y/n) ? ").
    symptom(Patient,felt_numb ) :- 
    verify(Patient," Felt numb or detached from people, activities, or your surroundings?(y/n) ? ").
    symptom(Patient, stressful_experience) :- 
    verify(Patient," Feeling very upset when something reminded you of a stressful experience from the past? (y/n) ? ").
    symptom(Patient,nightmares) :- 
    verify(Patient," Had nightmares about the event/s or thought about the event/s when you did not want to? (y/n) ? ").
    symptom(Patient,irritability) :- 
    verify(Patient," Do you have frequent feelings of irritability and aggressiveness (y/n) ? ").
    symptom(Patient,emptiness) :- 
    verify(Patient," Have you felt chronic emptiness or loneliness (y/n) ? ").
    symptom(Patient ,detachment) :- 
    verify(Patient," Have you experienced a pattern of detachment from social relationships (y/n) ? ").
    symptom(Patient,indifferent) :- 
    verify(Patient," Do you often feel indifferent to praise or criticisms from others? (y/n) ? ").
    symptom(Patient,reluctant) :- 
    verify(Patient," Are you reluctant to take personal risks or engage in new activities (y/n) ? ").
    symptom(Patient,self_doubt_overconfidence) :- 
    verify(Patient," My self-confidence ranges from GREAT self-doubt to EQUALLY GREAT overconfidence. (y/n) ? ").
    symptom(Patient,mentally_dul) :- 
    verify(Patient," Sometimes I am mentally dull and at other times I think VERY creatively. (y/n) ? ").
    symptom(Patient,optimism_pessimism) :- 
    verify(Patient," At some times I have GREAT optimism and at other times EQUALLY GREAT pessimism.(y/n) ? ").
    symptom(Patient,tearfulness) :- 
    verify(Patient," Some of the time I show MUCH tearfulness and crying and at other times I laugh and joke EXCESSIVELY (y/n) ? ").
    symptom(Patient,thoughts_hurting_yourself) :- 
    verify(Patient," Thoughts that you would be better off dead, or of hurting yourself (y/n) ? ").
    symptom(Patient,feeling_tired) :- 
    verify(Patient," Feeling tired or having little energy  (y/n) ? ").
    symptom(Patient,little_interest_in_doing_things) :- 
    verify(Patient," Little interest or pleasure in doing things (y/n) ? ").
    symptom(Patient,poor_appetite) :- 
    verify(Patient," Poor appetite or overeating (y/n) ? ").
    
    ask(Patient,Question) :-
        write(Patient),write(','),write(Question),
        read(N),
        ( (N == yes ; N == y)
          ->
           assert(yes(Question)) ;
           assert(no(Question)), fail).
        
    :- dynamic yes/1,no/1.		
        
    verify(P,S) :-
       (yes(S) -> true ; (no(S) -> fail ; ask(P,S))).
         
    undo :- retract(yes(_)),fail. 
    undo :- retract(no(_)),fail.
    undo.
        
    hypothesis(Patient,post_traumatic_stress_disorder) :-
    symptom(Patient,felt_numb),
    symptom(Patient,difficulty_concentrating),
    symptom(Patient,nightmares),
    symptom(Patient,stressful_experience).

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
    
    % hypothesis(Patient,depression) :-
    % symptom(Patient,felt_numb),
    % symptom(Patient,emptiness),
    % symptom(Patient,thoughts_hurting_yourself),
    % symptom(Patient,little_interest_in_doing_things),
    % symptom(Patient,poor_appetite),

        
        write_list([]).
    write_list([Term| Terms]) :-
    write(Term),
    write_list(Terms).
    
    
    response(Reply) :-
    get_single_char(Code),
    put_code(Code), nl,
    char_code(Reply, Code).

    incr(X, X1) :-
        X1 is X+1.