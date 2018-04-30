import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Random;

public class RandomGoing {

	public static void main(String[] args) throws IOException {
		long l = System.currentTimeMillis();
		PrintWriter out = new PrintWriter(new File("randomgoing.csv"));
		Random random = new Random();
		int n = 1000;
		int[] ans = new int[n];
		int iterations = 1000000;
		for (int q = 0; q < iterations; q++) {
			double dr = 1.0 / n;
			double x = 0.0;
			double y = 0.0;
			for (int i = 0; i < n; i++) {
				double alpha = random.nextDouble() * 2 * Math.PI;
				x += dr * Math.cos(alpha);
				y += dr * Math.sin(alpha);
			}
			double len = Math.sqrt(x * x + y * y);
			ans[(int) (len * n / 1.0)]++;
			if (q % 10000 == 0) {
				System.out.println(q);
				System.out.println(len);
				System.out.println(System.currentTimeMillis() - l);
			}
		}
		for (int i = 0; i < ans.length; i++) {
			out.println(i * 1.0 / n + "; " + ans[i] * 1.0 / iterations);
		}
		out.close();
	}

}
