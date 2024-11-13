// package spark.main;

// public class Main {
//     public static void main(String[] args) {
//         System.out.println("Hello world!");
//     }
// }
package spark.main;

import java.util.Arrays;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;

import scala.Tuple2;

public class Main {
	public static void main(String[] args) {
		SparkConf conf = new SparkConf().setMaster("spark://vtzy-Lenovo-Legion-7-15IMH05:7077").setAppName("Spark Word Count");
		try (JavaSparkContext sc = new JavaSparkContext(conf)) {
			JavaRDD<String> textFile = sc.textFile("hdfs://localhost:9000/input/input-1.txt");
			JavaPairRDD<String, Integer> result = textFile.flatMap(s -> Arrays.asList(s.split(" ")).iterator())
					.mapToPair(word -> new Tuple2<>(word, 1))
					.reduceByKey((a,b) -> (a+b));
			
			result.saveAsTextFile("hdfs://localhost:9000/output-spark/result");
		}
	}
}