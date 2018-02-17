package mmbbs;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class CalcTest {
  @Test
  public void evaluatesExpression() {
    Calc s = new Calc();
    int result=s.add(5, 2);
    assertEquals("Fehler beim Addieren",7.0, result,0.1);
  }
}