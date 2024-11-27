const char* dgemm_desc = "Blocked dgemm.";
const int BLOCK_SIZE = 64;

/* This routine performs a dgemm operation
 *
 *  C := C + A * B
 *
 * where A, B, and C are lda-by-lda matrices stored in column-major format.
 * On exit, A and B maintain their input values.
 */
void square_dgemm(int n, double* A, double* B, double* C) {
  // TODO: Implement the blocking optimization
  //       (The following is a placeholder naive three-loop dgemm)
  for (int i = 0; i < n; i += BLOCK_SIZE) {
    for (int j = 0; j < n; j += BLOCK_SIZE) {
      for (int k = 0; k < n; k += BLOCK_SIZE) {

        // Loop over each element within the current block
        for (int ii = i; ii < i + BLOCK_SIZE && ii < n; ++ii) {
          for (int jj = j; jj < j + BLOCK_SIZE && jj < n; ++jj) {
            double cij = C[ii + jj * n]; // Element C[ii][jj]
            for (int kk = k; kk < k + BLOCK_SIZE && kk < n; ++kk) {
              cij += A[ii + kk * n] * B[kk + jj * n]; // Update C[ii][jj]
            }
            C[ii + jj * n] = cij; // 
          }
        }  
      }
    }
  }
}