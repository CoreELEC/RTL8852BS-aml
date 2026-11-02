/******************************************************************************
 *
 * Copyright(c) 2012 - 2020 Realtek Corporation.
 *
 * This program is free software; you can redistribute it and/or modify it
 * under the terms of version 2 of the GNU General Public License as
 * published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
 * more details.
 *
 ******************************************************************************/
#ifdef PHL_FEATURE_NIC

#if defined(MAC_8852B_SUPPORT)
#ifdef MAC_FW_8852B_U2
#ifdef MAC_FW_CATEGORY_NICCE
extern u32 array_length_8852b_u2_nicce;
extern u8 array_8852b_u2_nicce[340616];
#endif /* MAC_FW_CATEGORY_NICCE */

#ifdef MAC_FW_CATEGORY_NIC_PLE
extern u32 array_length_8852b_u2_nic_ple;
extern u8 array_8852b_u2_nic_ple[280392];
#endif /* MAC_FW_CATEGORY_NIC_PLE */

#ifdef MAC_FW_CATEGORY_NIC
extern u32 array_length_8852b_u2_nic;
extern u8 array_8852b_u2_nic[275520];
#endif /* MAC_FW_CATEGORY_NIC */

#ifdef MAC_FW_CATEGORY_WOWLANCE
extern u32 array_length_8852b_u2_wowlance;
extern u8 array_8852b_u2_wowlance[275704];
#endif /* MAC_FW_CATEGORY_WOWLANCE */

#ifdef MAC_FW_CATEGORY_WOWLAN_PLE
extern u32 array_length_8852b_u2_wowlan_ple;
extern u8 array_8852b_u2_wowlan_ple[276776];
#endif /* MAC_FW_CATEGORY_WOWLAN_PLE */

#ifdef MAC_FW_CATEGORY_WOWLAN
extern u32 array_length_8852b_u2_wowlan;
extern u8 array_8852b_u2_wowlan[276584];
#endif /* MAC_FW_CATEGORY_WOWLAN */

#endif /* MAC_FW_8852B_U2 */
#ifdef MAC_FW_8852B_U3
#ifdef MAC_FW_CATEGORY_NICCE
extern u32 array_length_8852b_u3_nicce;
extern u8 array_8852b_u3_nicce[340536];
#endif /* MAC_FW_CATEGORY_NICCE */

#ifdef MAC_FW_CATEGORY_NIC_PLE
extern u32 array_length_8852b_u3_nic_ple;
extern u8 array_8852b_u3_nic_ple[280320];
#endif /* MAC_FW_CATEGORY_NIC_PLE */

#ifdef MAC_FW_CATEGORY_NIC
extern u32 array_length_8852b_u3_nic;
extern u8 array_8852b_u3_nic[275448];
#endif /* MAC_FW_CATEGORY_NIC */

#ifdef MAC_FW_CATEGORY_WOWLANCE
extern u32 array_length_8852b_u3_wowlance;
extern u8 array_8852b_u3_wowlance[275632];
#endif /* MAC_FW_CATEGORY_WOWLANCE */

#ifdef MAC_FW_CATEGORY_WOWLAN_PLE
extern u32 array_length_8852b_u3_wowlan_ple;
extern u8 array_8852b_u3_wowlan_ple[276704];
#endif /* MAC_FW_CATEGORY_WOWLAN_PLE */

#ifdef MAC_FW_CATEGORY_WOWLAN
extern u32 array_length_8852b_u3_wowlan;
extern u8 array_8852b_u3_wowlan[276512];
#endif /* MAC_FW_CATEGORY_WOWLAN */

#endif /* MAC_FW_8852B_U3 */
#endif /* #if MAC_XXXX_SUPPORT */
#endif /* PHL_FEATURE_NIC */
