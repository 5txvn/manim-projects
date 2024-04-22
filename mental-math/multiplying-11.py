from manim import *

class Main(Scene):
    def construct(self):
        #add the video sound
        self.add_sound("multiplying-by-11.mp3")
        #create the intro
        heart1 = ImageMobject("heart.png")
        heart1.shift(LEFT*5)
        heart1.shift(UP*2)
        heart1.rotate(PI/5)
        heart2 = ImageMobject("heart.png")
        heart2.shift(RIGHT*5.7)
        heart2.shift(UP*1.6)
        heart2.rotate(-PI/6)
        heart3 = ImageMobject("heart.png")
        heart3.shift(UP*2.5)
        heart4 = ImageMobject("heart.png")
        heart4.shift(LEFT*4.4)
        heart4.shift(DOWN*2.1)
        heart4.rotate(PI/4)
        heart5 = ImageMobject("heart.png")
        heart5.shift(RIGHT*5.2)
        heart5.shift(DOWN*2.35)
        heart5.rotate(-PI/8)
        heart6 = ImageMobject("heart.png")
        heart6.shift(DOWN*2.5)
        stevenlovesmath = Text("stevenlovesmath!")
        self.play(FadeIn(heart1),FadeIn(heart2),FadeIn(heart3),FadeIn(heart4),FadeIn(heart5),FadeIn(heart6),Write(stevenlovesmath),run_time=2)
        self.wait(3);
        self.play(FadeOut(heart1),FadeOut(heart2),FadeOut(heart3),FadeOut(heart4),FadeOut(heart5),FadeOut(heart6),FadeOut(stevenlovesmath),run_time=1.5)
        self.wait(1);
        #create the main title
        title = Text("Multiplying by 11")
        title.scale(1.5);
        self.play(Write(title),run_time=1.5);
        subtitle = Text("An animation by stevenlovesmath!",color=RED);
        self.wait(0.5);
        self.play(ApplyMethod(title.shift,UP*.5),run_time=1.5);
        subtitle.shift(DOWN*.8);
        self.play(Write(subtitle),run_time=2);
        self.wait(2)
        self.play(FadeOut(title),FadeOut(subtitle),run_time=2);
        self.wait(2)
        #set up first problem
        problem1 = MathTex(r"87 \times 11=\dots");
        problem1.scale(2);
        self.play(Write(problem1),run_time=2);
        self.wait(3);
        self.play(ApplyMethod(problem1.shift,UP*.5),run_time=1)
        num7 = Text("7",color=RED);
        num7.shift(DOWN*.5);
        self.play(Write(num7),run_time=1)
        self.wait(4);
        problem1with7 = MathTex(r"87 \times 11=\dots 7")
        problem1with7.scale(2)
        problem1with7.shift(UP*0.5)
        self.play(Transform(problem1,problem1with7),run_time=1)
        self.play(FadeOut(num7),run_time=1);
        self.play(ApplyMethod(problem1.shift,DOWN*.5),run_time=1);
        self.wait(3)
        start_point = np.array([3.5, -0.85, 0])
        end_point = np.array([1, -0.85, 0])
        arrow = Arrow(start=start_point,end=end_point,color=RED)
        self.play(Create(arrow),run_time=1)
        self.wait(2);
        self.play(FadeOut(arrow),run_time=1);
        self.wait(5);
        self.play(ApplyMethod(problem1.shift,UP*.5),run_time=1);
        addnums = Text("8+7=15",color=RED);
        addnums.shift(DOWN*.5);
        self.play(Write(addnums),run_time=2)
        problem1with57 = MathTex(r"87\times 11=\dots 57");
        problem1with57.scale(2);
        problem1with57.shift(UP*.5);
        self.wait(5);
        self.play(Transform(problem1,problem1with57),run_time=1);
        self.wait(4);
        self.play(FadeOut(addnums),run_time=1);
        self.play(ApplyMethod(problem1.shift,DOWN*.5),run_time=2);
        self.wait(7);
        self.play(ApplyMethod(problem1.shift,UP*.5),run_time=1);
        lastnum = Text("8+1=9",color=RED);
        lastnum.shift(DOWN*.5);
        self.play(Write(lastnum),run_time=1);
        self.wait(1);
        finalanswer = MathTex(r"87\times 11=957");
        finalanswer.scale(2);
        finalanswer.shift(UP*.5);
        self.play(Transform(problem1,finalanswer),run_time=1)
        self.play(FadeOut(lastnum),run_time=1)
        self.play(ApplyMethod(problem1.shift,DOWN*.5),run_time=1)
        self.wait(1);
        self.play(FadeOut(problem1),run_time=1);
        self.wait(4);
        problem2 = MathTex(r"323\times 11=\dots");
        problem2.scale(2);
        self.play(Write(problem2),run_time=3);
        self.wait(2);
        problem2with3 = MathTex(r"323\times 11=\dots 3");
        problem2with3.scale(2);
        self.play(Transform(problem2,problem2with3),run_time=1);
        self.wait(8);
        problem2with53 = MathTex(r"323\times 11=\dots 53");
        problem2with53.scale(2);
        self.play(Transform(problem2,problem2with53),run_time=1);
        self.wait(4);
        problem2with553 = MathTex(r"323\times 11=\dots 553");
        problem2with553.scale(2);
        self.play(Transform(problem2,problem2with553),run_time=1);
        self.wait(5);
        finalanswer = MathTex(r"323\times 11=3553");
        finalanswer.scale(2);
        self.play(Transform(problem2,finalanswer),run_time=1);
        self.wait(2);
        self.play(FadeOut(problem2),run_time=2);
        self.wait(2);
        finalproblem = MathTex(r"4157\times 11 =\dots")
        finalproblem.scale(2)
        self.play(Write(finalproblem),run_time=2);
        self.wait(2);
        finalproblemwith7 = MathTex(r"4157\times 11=\dots 7");
        finalproblemwith7.scale(2);
        self.play(Transform(finalproblem,finalproblemwith7),run_time=1);
        self.wait(6);
        finalproblemwith27 = MathTex(r"4157\times 11=\dots 27");
        finalproblemwith27.scale(2);
        self.play(Transform(finalproblem,finalproblemwith27),run_time=1);
        self.wait(6);
        finalproblemwith727 = MathTex(r"4157\times 11=\dots 727");
        finalproblemwith727.scale(2);
        self.play(Transform(finalproblem,finalproblemwith727),run_time=1);
        self.wait(3);
        finalproblemwith5727 = MathTex(r"4157\times 11=\dots 5727");
        finalproblemwith5727.scale(2);
        self.play(Transform(finalproblem,finalproblemwith5727),run_time=1);
        self.wait(3);
        finalanswer = MathTex(r"4157\times 11=45727");
        finalanswer.scale(2);
        self.play(Transform(finalproblem,finalanswer),run_time=1);
        self.wait(1);
        self.play(FadeOut(finalproblem),run_time=1);





        





