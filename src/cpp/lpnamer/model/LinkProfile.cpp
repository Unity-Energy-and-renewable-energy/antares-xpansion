//

#include "LinkProfile.h"

#include <exception>

#include "LogUtils.h"

constexpr int MAX_LINK_PROFILE_HOUR = NUMBER_OF_HOUR_PER_YEAR - 1;

double LinkProfile::getDirectProfile(size_t hour) const {
  if (hour > MAX_LINK_PROFILE_HOUR) {
    throw std::invalid_argument(
        LOGLOCATION +
        "Link profiles can be requested between point 0 and 8759.");
  }

  return direct_link_profile[hour];
}

double LinkProfile::getIndirectProfile(size_t hour) const {
  if (hour > MAX_LINK_PROFILE_HOUR) {
    throw std::invalid_argument(
        LOGLOCATION +
        "Link profiles can be requested between point 0 and 8759.");
  }

  return indirect_link_profile[hour];
}
