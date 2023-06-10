import java.util.Scanner;

public class StokGudang {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Stok Gudang Input Barang");
        System.out.println("########################");

        System.out.print("Masukkan nama anda: ");
        String nama = scanner.nextLine();

        System.out.println("\nSelamat Datang " + nama);

        System.out.print("Masukkan nama barang yang mau ditambah: ");
        String namaBarang = scanner.nextLine();

        System.out.print("Masukkan jumlah barang yang mau ditambah: ");
        int jumlahBarang = scanner.nextInt();

        System.out.print("Masukkan harga beli untuk barang tersebut: ");
        double hargaBeli = scanner.nextDouble();

        System.out.print("Masukkan harga jual untuk barang tersebut: ");
        double hargaJual = scanner.nextDouble();

        System.out.println("\nStok Gudang Rincian Barang");
        System.out.println("##########################");
        System.out.println("Nama Barang: " + namaBarang);
        System.out.println("Jumlah Barang: " + jumlahBarang);
        System.out.printf("Harga Beli: Rp. %.2f\n", hargaBeli);
        System.out.printf("Harga Jual: Rp. %.2f\n", hargaJual);

        scanner.close();
    }
}
