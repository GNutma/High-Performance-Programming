/* forkJoin.c
 * ... illustrates the fork-join pattern 
 *      using OpenMP's parallel directive.
 *
 * Huib Aldewereld, HU
 *
 * Compile by: gcc -fopenmp -o forkJoin forkJoin.c
 *
 * Usage: ./forkJoin
 *
 * Exercise:
 * - Compile & run, uncomment the pragma,
 *    recompile & run, compare results.
 */

#include <stdio.h>     // printf()
#include <omp.h>       // OpenMP

int main(int argc, char** argv) {

    printf("\nBefore...\n");

   #pragma omp parallel num_threads(4)
    printf("\nDuring...");

    printf("\n\nAfter...\n\n");

    return 0;
}
