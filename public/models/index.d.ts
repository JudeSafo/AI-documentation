import { ModelInit, MutableModel, __modelMeta__, ManagedIdentifier } from "@aws-amplify/datastore";
// @ts-ignore
import { LazyLoading, LazyLoadingDisabled } from "@aws-amplify/datastore";





type EagerTest = {
  readonly [__modelMeta__]: {
    identifier: ManagedIdentifier<Test, 'id'>;
    readOnlyFields: 'createdAt' | 'updatedAt';
  };
  readonly id: string;
  readonly userID: string;
  readonly userEMAIL?: string | null;
  readonly userCompany?: string | null;
  readonly userROLE?: string | null;
  readonly createdAt?: string | null;
  readonly updatedAt?: string | null;
}

type LazyTest = {
  readonly [__modelMeta__]: {
    identifier: ManagedIdentifier<Test, 'id'>;
    readOnlyFields: 'createdAt' | 'updatedAt';
  };
  readonly id: string;
  readonly userID: string;
  readonly userEMAIL?: string | null;
  readonly userCompany?: string | null;
  readonly userROLE?: string | null;
  readonly createdAt?: string | null;
  readonly updatedAt?: string | null;
}

export declare type Test = LazyLoading extends LazyLoadingDisabled ? EagerTest : LazyTest

export declare const Test: (new (init: ModelInit<Test>) => Test) & {
  copyOf(source: Test, mutator: (draft: MutableModel<Test>) => MutableModel<Test> | void): Test;
}