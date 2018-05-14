classdefs = {
"CommentMarker"                           : ("0d010101-0101-0800-060e-2b3402060101", "Event", True, {
    "CommentMarkerAnnotationList"            : ("6d64dd66-e5c7-488f-b0e4-272c932378a6", 0xFFDA, "aafString", True, False),
    "CommentMarkerAttributeList"             : ("c72cc817-aac5-499b-af34-bc47fec1eaa8", 0xFFD7, "kAAFTypeID_TaggedValueStrongReferenceVector", True, False),
    "CommentMarkerColor"                     : ("e96e6d44-c383-11d3-a069-006094eb75cb", 0xFFDE, "RGBColor", True, False),
    "CommentMarkerDate"                      : ("c4c45d9b-0967-11d4-a08a-006094eb75cb", 0xFFDC, "aafString", True, False),
    "CommentMarkerIcon"                      : ("c4c45d9d-0967-11d4-a08a-006094eb75cb", 0xFFD9, "aafInt32", True, False),
    "CommentMarkerStatus"                    : ("c4c45d9e-0967-11d4-a08a-006094eb75cb", 0xFFD8, "aafInt32", True, False),
    "CommentMarkerTime"                      : ("c4c45d9c-0967-11d4-a08a-006094eb75cb", 0xFFDB, "aafString", True, False),
    "CommentMarkerUser"                      : ("c4c45d9a-0967-11d4-a08a-006094eb75cb", 0xFFDD, "aafString", True, False),
    }
),
"TapeDescriptor"                          : ("0d010101-0101-2e00-060e-2b3402060101", "EssenceDescriptor", True, {
    "ColorFrame"                             : ("9548b03a-15fb-11d4-a08f-006094eb75cb", 0xFFDF, "aafInt32", True, False),
    }
),
"PCMDescriptor"                           : ("0d010101-0101-4800-060e-2b3402060101", "SoundDescriptor", True, {
    "DataOffset"                             : ("bb3fabdd-fcc0-43a8-9759-c727771fcc4a", 0xFFE0, "aafInt32", True, False),
    }
),
"CDCIDescriptor"                          : ("0d010101-0101-2800-060e-2b3402060101", "DigitalImageDescriptor", True, {
    "ImageStartAlignment"                    : ("506f8de5-54a1-11d3-a029-006094eb75cb", 0xFFE2, "aafUInt32", True, False),
    "OffsetToFrameIndexes"                   : ("9d15fca3-54c5-11d3-a029-006094eb75cb", 0xFFE4, "aafInt32", True, False),
    "OffsetToFrameIndexes64"                 : ("298eb260-30b6-4e30-8c90-cf63aa793c34", 0xFFE3, "aafInt64", True, False),
    }
),
"DigitalImageDescriptor"                  : ("0d010101-0101-2700-060e-2b3402060101", "FileDescriptor", False, {
    "AvidEssenceElementSizeKind"             : ("0e040101-0101-0110-060e-2b3401010101", 0xFFE5, "AvidEssenceElementSizeKind", True, False),
    "DataOffset"                             : ("bfde81e4-bcc8-4abd-a80e-214dc0f14684", 0xFFEB, "aafInt32", True, False),
    "EssenceBox"                             : ("0e040101-0101-0107-060e-2b3401010101", 0xFFE7, "BoundsBox", True, False),
    "FirstFrameOffset"                       : ("ce2aca4e-51ab-11d3-a024-006094eb75cb", 0xFFEF, "aafInt32", True, False),
    "FrameIndexByteOrder"                    : ("b57e925d-170d-11d4-a08f-006094eb75cb", 0xFFEC, "aafUInt16", True, False),
    "FrameSampleSize"                        : ("ce2aca50-51ab-11d3-a024-006094eb75cb", 0xFFED, "aafInt32", True, False),
    "FrameStartOffset"                       : ("c8a0bd74-a247-4297-a52c-4458bffa1fc6", 0xFFEA, "aafInt32", True, False),
    "FramingBox"                             : ("0e040101-0101-010c-060e-2b3401010101", 0xFFE9, "BoundsBox", True, False),
    "ImageSize"                              : ("ce2aca4f-51ab-11d3-a024-006094eb75cb", 0xFFEE, "aafInt32", True, False),
    "ResolutionID"                           : ("ce2aca4d-51ab-11d3-a024-006094eb75cb", 0xFFF0, "aafInt32", True, False),
    "SourceBox"                              : ("0e040101-0101-0108-060e-2b3401010101", 0xFFE6, "BoundsBox", True, False),
    "ValidBox"                               : ("0e040101-0101-0106-060e-2b3401010101", 0xFFE8, "BoundsBox", True, False),
    }
),
"ANCDataDescriptor"                       : ("0d010101-0101-5c00-060e-2b3402060101", "DataEssenceDescriptor", True, {
    "ManifestArray"                          : ("0e040101-0101-0105-060e-2b3401010101", 0xFFCE, "AvidManifestArray", True, False),
    }
),
"VaryingValue"                            : ("0d010101-0101-3e00-060e-2b3402060101", "Parameter", True, {
    "VVal_Extrapolation"                     : ("8f2b8bae-b685-4939-b3a5-6373633b3e6c", 0xFFB8, "AUID", True, False),
    "VVal_FieldCount"                        : ("2902558b-acfa-439e-a1cd-9fa1e8f891ef", 0xFFB9, "aafInt16", True, False),
    }
),
"DataEssenceDescriptor"                   : ("0d010101-0101-4300-060e-2b3402060101", "FileDescriptor", True, {
    "DataOffset"                             : ("0e040101-0101-0109-060e-2b3401010101", 0xFFD3, "aafInt32", True, False),
    "FirstFrameOffset"                       : ("0e040101-0101-0102-060e-2b3401010101", 0xFFD1, "aafInt32", True, False),
    "MaxSampleSize"                          : ("0e040101-0101-0104-060e-2b3401010101", 0xFFCF, "aafInt32", True, False),
    "MinSampleSize"                          : ("0e040101-0101-0103-060e-2b3401010101", 0xFFD0, "aafInt32", True, False),
    "OffsetToFrameIndexes"                   : ("0e040101-0101-0101-060e-2b3401010101", 0xFFD2, "aafInt64", True, False),
    }
),
"Parameter"                               : ("0d010101-0101-3c00-060e-2b3402060101", "InterchangeObject", False, {
    "IsEnabled"                              : ("0e040101-0101-010b-060e-2b3401010101", 0xFFD4, "Boolean", True, False),
    "IsSilent"                               : ("967dbcc7-4ba6-4b57-b8e8-3a0fbc550353", 0xFFD5, "Boolean", True, False),
    }
),
"ScopeReference"                          : ("0d010101-0101-0d00-060e-2b3402060101", "Segment", True, {
    "Avid Scope"                             : ("9dc9c6cb-479d-4ff6-988a-b6784b90dc43", 0xFFCD, "aafUInt32", True, False),
    }
),
"Component"                               : ("0d010101-0101-0200-060e-2b3402060101", "InterchangeObject", False, {
    "ComponentAttributeList"                 : ("60958184-47b1-11d4-a01c-0004ac969f50", 0xFFCC, "kAAFTypeID_TaggedValueStrongReferenceVector", True, False),
    }
),
"Mob"                                     : ("0d010101-0101-3400-060e-2b3402060101", "InterchangeObject", False, {
    "AppCode"                                : ("96c46992-4f62-11d3-a022-006094eb75cb", 0xFFFA, "aafInt32", True, False),
    "ConvertFrameRate"                       : ("d4243bd4-0142-4595-a8f3-f2eba54244de", 0xFFF8, "Boolean", True, False),
    "FileMobRate"                            : ("0e040101-0101-010f-060e-2b3401010101", 0xFFF5, "Rational", True, False),
    "MobAttributeList"                       : ("60958183-47b1-11d4-a01c-0004ac969f50", 0xFFF9, "kAAFTypeID_TaggedValueStrongReferenceVector", True, False),
    "SubclipBegin"                           : ("aa24b657-fcbb-4921-951d-3a2038396722", 0xFFF6, "aafInt64", True, False),
    "SubclipFullLength"                      : ("1262bf7b-fce2-4dfe-a0f6-ceec047c80aa", 0xFFF7, "aafInt64", True, False),
    }
),
"SubDescriptor"                           : ("0d010101-0101-5900-060e-2b3402060101", "InterchangeObject", False, {
    }
),
"SourceClip"                              : ("0d010101-0101-1100-060e-2b3402060101", "SourceReference", True, {
    "SubclipFullLength"                      : ("660162e5-bbef-4618-8e0b-4b149b661a12", 0xFFD6, "aafInt64", True, False),
    }
),
"EssenceDescriptor"                       : ("0d010101-0101-2400-060e-2b3402060101", "InterchangeObject", False, {
    "MediaContainer"                         : ("13980e2b-2f30-44ec-bdb0-3b730da56562", 0xFFF1, "aafString", True, False),
    "MediaContainerGUID"                     : ("92790417-0131-4a05-898d-167691e11ca1", 0xFFF2, "AUID", True, False),
    "SubDescriptors"                         : ("06010104-0610-0000-060e-2b3401010109", 0xFFF3, "kAAFTypeID_SubDescriptorStrongReferenceVector", True, False),
    }
),
"AvidTrackManTrackedParamClass"           : ("30a42454-069e-11d4-9ffb-0004ac969f50", "InterchangeObject", True, {
    "TKMNTrackedParamSetngs"                 : ("30a42453-069e-11d4-9ffb-0004ac969f50", 0xFF9F, "AvidBagOfBits", False, False),
    }
),
"TimelineMobSlot"                         : ("0d010101-0101-3b00-060e-2b3402060101", "MobSlot", True, {
    "TimelineMobAttributeList"               : ("107f8331-1914-4234-b2c4-5a3eb755b7ca", 0xFFF4, "kAAFTypeID_TaggedValueStrongReferenceVector", True, False),
    }
),
"ControlPoint"                            : ("0d010101-0101-1900-060e-2b3402060101", "InterchangeObject", True, {
    "ControlPointPointProperties"            : ("3c1b48d0-c32c-4ea9-bb9d-35b898527283", 0xFFBE, "kAAFTypeID_ParameterStrongReferenceVector", True, False),
    "ControlPointSource"                     : ("0e040101-0101-010a-060e-2b3401010101", 0xFFBD, "aafInt32", True, False),
    }
),
"Transition"                              : ("0d010101-0101-1700-060e-2b3402060101", "Component", True, {
    "TranTKMNTrackedParamAry"                : ("2c04d7ec-179d-11d4-a003-0004ac969f50", 0xFFBB, "AvidTKMNTrackedParamArray", True, False),
    "TranTKMNTrackedParamSetngs"             : ("2c04d7ed-179d-11d4-a003-0004ac969f50", 0xFFBA, "AvidBagOfBits", True, False),
    "TranTKMNTrackerDataAry"                 : ("2c04d7eb-179d-11d4-a003-0004ac969f50", 0xFFBC, "AvidTKMNTrackerDataArray", True, False),
    }
),
"TaggedValue"                             : ("0d010101-0101-3f00-060e-2b3402060101", "InterchangeObject", True, {
    "PortableObject"                         : ("b6bb5f4e-7b37-11d3-a044-006094eb75cb", 0xFFC9, "AvidStrongReference", True, False),
    "PortableObjectClassID"                  : ("08835f4f-7b28-11d3-a044-006094eb75cb", 0xFFCA, "aafUInt32", True, False),
    "TaggedValueAttributeList"               : ("60958185-47b1-11d4-a01c-0004ac969f50", 0xFFCB, "kAAFTypeID_TaggedValueStrongReferenceVector", True, False),
    "TaggedValue_Stream"                     : ("c12d81ac-bd68-4fef-a37f-562d28e37158", 0xFFC8, "Stream", True, False),
    }
),
"EdgeCode"                                : ("0d010101-0101-0400-060e-2b3402060101", "Segment", True, {
    "AvBasePerf"                             : ("1fb0160a-6907-45fe-a997-c6818820970e", 0xFFB2, "aafUInt8", True, False),
    "AvEdgeType"                             : ("4d783cfa-35da-4566-9a52-2190d5078616", 0xFFB3, "aafInt16", True, False),
    "AvFilmType"                             : ("067da182-a750-48ba-995b-b7fd88f3b838", 0xFFB4, "aafInt16", True, False),
    }
),
"RGBADescriptor"                          : ("0d010101-0101-2900-060e-2b3402060101", "DigitalImageDescriptor", True, {
    "OffsetToFrameIndexes"                   : ("0e040101-0101-010d-060e-2b3401010101", 0xFFE1, "aafInt64", True, False),
    }
),
"AvidTrackManTrackerDataClass"            : ("13e0a981-0412-11d4-9ff9-0004ac969f50", "InterchangeObject", True, {
    "TKMNTrkDataBoxX"                        : ("e3c9057c-311d-41c1-9a7d-41ae1de90150", 0xFFA1, "kAAFTypeID_ParameterStrongReference", True, False),
    "TKMNTrkDataBoxY"                        : ("f15129da-7d1a-4f68-87ab-c0956f125654", 0xFFA0, "kAAFTypeID_ParameterStrongReference", True, False),
    "TKMNTrkDataConfidence"                  : ("c63c3449-0412-11d4-9ff9-0004ac969f50", 0xFFAE, "kAAFTypeID_ParameterStrongReference", True, False),
    "TKMNTrkDataDataX"                       : ("c63c3447-0412-11d4-9ff9-0004ac969f50", 0xFFB0, "kAAFTypeID_ParameterStrongReference", True, False),
    "TKMNTrkDataDataY"                       : ("c63c3448-0412-11d4-9ff9-0004ac969f50", 0xFFAF, "kAAFTypeID_ParameterStrongReference", True, False),
    "TKMNTrkDataFilterDataAmt"               : ("aab41ed6-07cc-4917-8119-a4bfeec607a0", 0xFFA2, "Rational", True, False),
    "TKMNTrkDataJitterRemovalEnabled"        : ("d1f936be-6f3a-4b8d-8e7a-855ab8a8565f", 0xFFA3, "Boolean", True, False),
    "TKMNTrkDataOffsetTrackingEnabled"       : ("875d33e9-f596-4daa-9730-3128a06b9763", 0xFFA5, "Boolean", True, False),
    "TKMNTrkDataOffsetX"                     : ("c63c344a-0412-11d4-9ff9-0004ac969f50", 0xFFAD, "kAAFTypeID_ParameterStrongReference", True, False),
    "TKMNTrkDataOffsetY"                     : ("c63c344b-0412-11d4-9ff9-0004ac969f50", 0xFFAC, "kAAFTypeID_ParameterStrongReference", True, False),
    "TKMNTrkDataPatternH"                    : ("c63c344d-0412-11d4-9ff9-0004ac969f50", 0xFFAA, "kAAFTypeID_ParameterStrongReference", True, False),
    "TKMNTrkDataPatternW"                    : ("c63c344c-0412-11d4-9ff9-0004ac969f50", 0xFFAB, "kAAFTypeID_ParameterStrongReference", True, False),
    "TKMNTrkDataSearchBH"                    : ("c63c3451-0412-11d4-9ff9-0004ac969f50", 0xFFA6, "kAAFTypeID_ParameterStrongReference", True, False),
    "TKMNTrkDataSearchLW"                    : ("c63c344e-0412-11d4-9ff9-0004ac969f50", 0xFFA9, "kAAFTypeID_ParameterStrongReference", True, False),
    "TKMNTrkDataSearchRW"                    : ("c63c344f-0412-11d4-9ff9-0004ac969f50", 0xFFA8, "kAAFTypeID_ParameterStrongReference", True, False),
    "TKMNTrkDataSearchTH"                    : ("c63c3450-0412-11d4-9ff9-0004ac969f50", 0xFFA7, "kAAFTypeID_ParameterStrongReference", True, False),
    "TKMNTrkDataSettings"                    : ("c63c3452-0412-11d4-9ff9-0004ac969f50", 0xFFB1, "AvidBagOfBits", False, False),
    "TKMNTrkDataSmoothingEnabled"            : ("75994f5f-e038-4769-9026-d8082cebc6e0", 0xFFA4, "Boolean", True, False),
    }
),
"OperationGroup"                          : ("0d010101-0101-0a00-060e-2b3402060101", "Segment", True, {
    "OpGroupAVXParamStream"                  : ("b045db5e-87d7-47fb-b862-2a548a1cad60", 0xFFC1, "Stream", True, False),
    "OpGroupGraphicsParamStream"             : ("73fe71c5-15f3-4f0e-acb8-b70edfe6ca5c", 0xFFC2, "Stream", True, False),
    "OpGroupLeftLength"                      : ("7cd5da62-6a1c-4490-9f6c-f57204ec7dba", 0xFFC0, "aafInt32", True, False),
    "OpGroupMotionCtlOffsetMapAdjust"        : ("77ad6841-08fc-4f53-bd0a-2a6b0b5f94d9", 0xFFC4, "Rational", True, False),
    "OpGroupMotionCtlSourceParams"           : ("614406f1-d8e7-469b-bd99-0e70a9a9cd60", 0xFFC3, "kAAFTypeID_ParameterStrongReferenceVector", True, False),
    "OpGroupRightLength"                     : ("a7da7356-2021-4f89-97d2-e683307c8dd7", 0xFFBF, "aafInt32", True, False),
    "OpGrpTKMNTrackedParamAry"               : ("30a42451-069e-11d4-9ffb-0004ac969f50", 0xFFC6, "AvidTKMNTrackedParamArray", True, False),
    "OpGrpTKMNTrackedParamSetng"             : ("30a42452-069e-11d4-9ffb-0004ac969f50", 0xFFC5, "AvidBagOfBits", True, False),
    "OpGrpTKMNTrackerDataAry"                : ("af913551-04c3-11d4-9ff9-0004ac969f50", 0xFFC7, "AvidTKMNTrackerDataArray", True, False),
    }
),
"Header"                                  : ("0d010101-0101-2f00-060e-2b3402060101", "InterchangeObject", True, {
    "AudioRateAdjustmentFactor"              : ("b7d51ad5-650b-4d3a-8596-99b579e177a6", 0xFFFB, "aafUInt16", True, False),
    "EssenceFileMobID"                       : ("abf1b771-8efd-4802-8b2f-680dff611381", 0xFFFE, "MobIDType", True, False),
    "MasterMobID"                            : ("ffdd41e1-ae2c-49c6-ae58-78e041454179", 0xFFFF, "MobIDType", True, False),
    "ProjectEditRate"                        : ("f36546b1-387c-4ee9-8c70-a718467ae486", 0xFFFC, "Rational", True, False),
    "ProjectName"                            : ("62fc3717-492d-42bf-a5fb-7b25f61594b9", 0xFFFD, "aafString", True, False),
    }
),
"EssenceGroup"                            : ("0d010101-0101-0500-060e-2b3402060101", "Segment", True, {
    "EssenceGroupType"                       : ("d9c9bf24-f6b8-11d3-a083-006094eb75cb", 0xFFB5, "aafInt32", True, False),
    }
),
"Avid MC Mob Reference"                   : ("6619f8e0-fe77-11d3-a084-006094eb75cb", "InterchangeObject", True, {
    "Mob Reference MobID"                    : ("81110e9f-fe7c-11d3-a084-006094eb75cb", 0xFFB7, "MobIDType", False, False),
    "Mob Reference Position"                 : ("81110ea0-fe7c-11d3-a084-006094eb75cb", 0xFFB6, "aafInt64", False, False),
    }
),
}

aliases = {
"Avid_MC_Mob_Reference"                   : "Avid MC Mob Reference",
}
