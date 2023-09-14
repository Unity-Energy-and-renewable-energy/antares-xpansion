//
// Created by marechaljas on 08/11/22.
//

#pragma once

#include "../../lpnamer/model/Problem.h"
class IProblemWriter {
 public:
  virtual ~IProblemWriter() = default;
  virtual void Write_problem(Problem *in_prblm) = 0;
};
