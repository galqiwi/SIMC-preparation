
public class Singapore {

	public static void main(String[] args) {
		long l = System.currentTimeMillis();
		int r = 2000;
		boolean[][] island = new boolean[2 * r + 1][2 * r + 1];
		double dr = 1.0 / r;
		island[r][r] = true;
		double x = 1.0;
		double y = 1.0;
		int sum = 0;
		for (int i = 0; i < island.length; i++) {
			for (int j = 0; j < island.length; j++) {
				if (Math.sqrt((r - i) * (r - i) + (r - j) * (r - j)) * dr <= 1) {
					sum++;
				}
			}
		}
		double alpha = 0;
		double rad = 0;
		double phi = 0;
		for (int i = 1; i <= r; i++) {
			alpha += 6.704411641425197 * dr / Math.sqrt(alpha * alpha + 1);
			rad = alpha / 6.704411641425197;
			double x1 = x;
			double y1 = y;
			x = 1 + rad * Math.cos(alpha);
			y = 1 + rad * Math.sin(alpha);
			for (int a = 0; a < island.length; a++) {
				for (int b = 0; b < island.length; b++) {
					if (Math.sqrt((r - a) * (r - a) + (r - b) * (r - b)) * dr <= 1
							&& Math.sqrt((x - a * dr) * (x - a * dr) + (y - b * dr) * (y - b * dr)) <= i * dr / 2) {
						island[a][b] = true;
					}
				}
			}
			System.out.println(i + " " + (System.currentTimeMillis() - l) + " " + x + " " + y + " " + phi + " "
					+ Math.sqrt((x - 1) * (x - 1) + (y - 1) * (y - 1)) + " "
					+ Math.sqrt((x - x1) * (x - x1) + (y - y1) * (y - y1)));
		}
		int th = 0;
		for (int a = 0; a < island.length; a++) {
			for (int b = 0; b < island.length; b++) {
				if (island[a][b]) {
					th++;
				}
			}
		}
		System.out.println(System.currentTimeMillis() - l);
		System.out.println(th * 1.0 / sum);
	}

}
