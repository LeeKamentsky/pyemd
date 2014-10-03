/*
 * pyemd is licensed under the BSD license. See the accompanying file LICENSE
 * for details.
 *
 * Copyright (c) 2014 Broad Institute
 *
 * This file provides templates of all the given flow types
 * so that Cython only has templates of the numeric types.
 */
#include "emd_hat.hpp"

template<typename NUM_T>
NUM_T emd_hat_gd_metric_no_flow(
    const std::vector<NUM_T> & P,
    const std::vector<NUM_T> & Q,
    const std::vector< std::vector<NUM_T> > &C,
    NUM_T extra_mass_penalty=-1,
    std::vector< std::vector<NUM_T> > *F=NULL)
{
    return emd_hat_gd_metric<NUM_T>()(P, Q, C, extra_mass_penalty, F);
}

template<typename NUM_T>
NUM_T emd_hat_gd_metric_without_transshipment_flow (
    const std::vector<NUM_T> & P,
    const std::vector<NUM_T> & Q,
    const std::vector< std::vector<NUM_T> > &C,
    NUM_T extra_mass_penalty=-1,
    std::vector< std::vector<NUM_T> > *F=NULL) 
{
    return emd_hat_gd_metric<NUM_T, WITHOUT_TRANSHIPMENT_FLOW>()(
             P, Q, C, extra_mass_penalty, F);
}

template<typename NUM_T>
NUM_T emd_hat_gd_metric_without_extra_mass_flow(
    const std::vector<NUM_T> & P,
    const std::vector<NUM_T> & Q,
    const std::vector< std::vector<NUM_T> > &C,
    NUM_T extra_mass_penalty=-1,
    std::vector< std::vector<NUM_T> > *F=NULL) 
{
    return emd_hat_gd_metric<NUM_T, WITHOUT_EXTRA_MASS_FLOW>()(
             P, Q, C, extra_mass_penalty, F);
}

template<typename NUM_T>
NUM_T emd_hat_no_flow(
    const std::vector<NUM_T> & P,
    const std::vector<NUM_T> & Q,
    const std::vector< std::vector<NUM_T> > &C,
    NUM_T extra_mass_penalty=-1,
    std::vector< std::vector<NUM_T> > *F=NULL) 
{
    return emd_hat<NUM_T>()(P, Q, C, extra_mass_penalty, F);
}

template<typename NUM_T>
NUM_T emd_hat_without_transshipment_flow(
    const std::vector<NUM_T> & P,
    const std::vector<NUM_T> & Q,
    const std::vector< std::vector<NUM_T> > &C,
    NUM_T extra_mass_penalty=-1,
    std::vector< std::vector<NUM_T> > *F=NULL) 
{
    return emd_hat<NUM_T, WITHOUT_TRANSHIPMENT_FLOW>()(
             P, Q, C, extra_mass_penalty, F);
}

template<typename NUM_T>
NUM_T emd_hat_without_extra_mass_flow(
    const std::vector<NUM_T> & P,
    const std::vector<NUM_T> & Q,
    const std::vector< std::vector<NUM_T> > &C,
    NUM_T extra_mass_penalty=-1,
    std::vector< std::vector<NUM_T> > *F=NULL) 
{
    return emd_hat<NUM_T, WITHOUT_EXTRA_MASS_FLOW>()(
             P, Q, C, extra_mass_penalty, F);
}

