from manim import *

class Sandbox(Scene):
    def construct(self):
        A = np.array([-1,-1,0]);
        B = np.array([-1,5/4,0]);
        C = np.array([2,-1,0]);
        triangle1 = Polygon(A,B,C);
        triangle2 = Polygon(A,B,C);
        triangle3 = Polygon(A,B,C);
        triangle4 = Polygon(A,B,C);
        A1 = np.array([-3,-3,0]);
        B1 = np.array([-3,5/17*6-3,0]);
        C1 = np.array([12/17*6-3,-3,0]);
        A2 = np.array([-3,5/17*6-3,0]);
        B2 = np.array([-3,3,0]);
        C2 = np.array([5/17*6-3,3,0]);

        A3 = np.array([5/17*6-3,3,0]);
        B3 = np.array([3,3,0]);
        C3 = np.array([3,12/17*6-3,0]);
        A4 = np.array([3,12/17*6-3,0]);
        B4 = np.array([3,-3,0]);
        C4 = np.array([12/17*6-3,-3,0])
        self.play(Create(triangle1),Create(triangle2),Create(triangle3),Create(triangle4),run_time=2);
        self.play(Transform(triangle1,Polygon(A1,B1,C1)),Transform(triangle2,Polygon(A2,B2,C2)),Transform(triangle3,Polygon(A3,B3,C3)),Transform(triangle4,Polygon(A4,B4,C4)));

        aGroup = VGroup(Text("a").move_to([-2.25,3.5,0]),Text("a").move_to([3.5,2.25,0]),Text("a").move_to([2.25,-3.5,0]),Text("a").move_to([-3.5,-2.25,0]));
        for text in aGroup:
            text.set_fill(YELLOW)
        bGroup = VGroup(Text("b").move_to([.75,3.5,0]),Text("b").move_to([3.5,-.75,0]),Text("b").move_to([-.75,-3.5,0]),Text("b").move_to([-3.5,.75,0]));
        cGroup = VGroup(Text("c").move_to([-1.62,.62,0]),Text("c").move_to([.62,1.62,0]),Text("c").move_to([1.62,-.62,0]),Text("c").move_to([-.62,-1.62,0]));
        for text in cGroup:
            text.set_fill(GREEN)
        self.play(Write(aGroup),run_time=1)
        self.play(Write(bGroup),run_time=1)
        self.play(Write(cGroup),run_time=1)