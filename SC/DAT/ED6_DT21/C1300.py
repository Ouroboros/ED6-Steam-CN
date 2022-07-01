import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1300_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1300   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '穆拉'),
    TXT(0x02, '朵洛希'),
    TXT(0x03, '士兵'),
    TXT(0x04, '士兵'),
    TXT(0x05, '士兵'),
    TXT(0x06, '士兵'),
    TXT(0x07, '士兵'),
    TXT(0x08, '士兵'),
    TXT(0x09, '士兵'),
    TXT(0x0A, '空贼船'),
    TXT(0x0B, '空贼船（影）'),
    TXT(0x0C, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1300.x'
    header.mapIndex       = 52
    header.bgm            = 89
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x323E
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT27/CH03570._CH', 'ED6_DT27/CH03570P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT06/CH20063._CH', 'ED6_DT06/CH20063P._CP'),
        ('ED6_DT06/CH20064._CH', 'ED6_DT06/CH20064P._CP'),
        ('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP'),
        ('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP'),
        ('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP'),
        ('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP'),
        ('ED6_DT07/CH00290._CH', 'ED6_DT07/CH00290P._CP'),
        ('ED6_DT07/CH00291._CH', 'ED6_DT07/CH00291P._CP'),
        ('ED6_DT07/CH00300._CH', 'ED6_DT07/CH00300P._CP'),
        ('ED6_DT07/CH00301._CH', 'ED6_DT07/CH00301P._CP'),
        ('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP'),
        ('ED6_DT27/CH04571._CH', 'ED6_DT27/CH04571P._CP'),
        ('ED6_DT27/CH04572._CH', 'ED6_DT27/CH04572P._CP'),
        ('ED6_DT07/CH00321._CH', 'ED6_DT07/CH00321P._CP'),
        ('ED6_DT06/CH20043._CH', 'ED6_DT06/CH20043P._CP'),
        ('ED6_DT07/CH00326._CH', 'ED6_DT07/CH00326P._CP'),
        ('ED6_DT07/CH00320._CH', 'ED6_DT07/CH00320P._CP'),
        ('ED6_DT27/CH03010._CH', 'ED6_DT27/CH03010P._CP'),
        ('ED6_DT27/CH03011._CH', 'ED6_DT27/CH03011P._CP'),
        ('ED6_DT27/CH03101._CH', 'ED6_DT27/CH03101P._CP'),
        ('ED6_DT27/CH03014._CH', 'ED6_DT27/CH03014P._CP'),
        ('ED6_DT27/CH03761._CH', 'ED6_DT27/CH03761P._CP'),
        ('ED6_DT27/CH03771._CH', 'ED6_DT27/CH03771P._CP'),
    ]

# id: 0x10002 offset: 0x17A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x2DA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x2DA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x2DA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -9880,
            triggerZ            = 4000,
            triggerY            = -550,
            triggerRange        = 1500,
            actorX              = -8980,
            actorZ              = 5200,
            actorY              = -340,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0010,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2FE
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 4, 0x1804)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_30A',
    )

    Event(0, 0x0002)

    def _loc_30A(): pass

    label('loc_30A')

    Return()

# id: 0x0001 offset: 0x30B
@scena.Code('Init')
def Init():
    OP_72(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    OP_A1(0x0011, 0x0000)
    OP_A1(0x0012, 0x0001)
    SetChrPos(0x0011, -2160, 0, -1510, 0)
    SetChrPos(0x0012, -2160, 100, -1510, 0)
    OP_8C(0x0011, 350, 0)
    OP_8C(0x0012, 350, 0)

    Return()

# id: 0x0002 offset: 0x350
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_6D(-17010, 4000, -16370, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    CreateThread(0x0129, 0x01, 0x00, 0x0003)
    Sleep(500)

    CreateThread(0x012A, 0x01, 0x00, 0x0004)
    Sleep(500)

    CreateThread(0x0146, 0x01, 0x00, 0x0005)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, 0x0006)
    WaitForThreadExit(0x0129, 0x0001)
    OP_8C(0x0129, 0, 400)

    ChrTalk(
        0x0129,
        (
            '#0300280241V#192F#2P哦哦……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0404')
    def lambda_0404():
        OP_6D(-7610, 4000, -1690, 7000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_0404)

    @scena.Lambda('lambda_041C')
    def lambda_041C():
        OP_67(0, 5790, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_041C)

    @scena.Lambda('lambda_0434')
    def lambda_0434():
        OP_6E(255, 7000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0434)

    @scena.Lambda('lambda_0444')
    def lambda_0444():
        OP_6B(4660, 7000)

        ExitThread()

    DispatchAsync(0x0129, 0x0003, lambda_0444)

    CreateThread(0x0129, 0x01, 0x00, 0x0007)
    Sleep(300)

    CreateThread(0x012A, 0x01, 0x00, 0x0008)
    Sleep(300)

    CreateThread(0x0146, 0x01, 0x00, 0x0009)
    Sleep(400)

    CreateThread(0x0102, 0x01, 0x00, 0x000A)
    WaitForThreadExit(0x0146, 0x0001)

    ChrTalk(
        0x0129,
        (
            '#0300280242V#191F#6P可爱的『山猫号』……\n',
            '真是想死你了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280243V#211F看起来\n',
            '保养得很好呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012A,
        (
            '#0290280244V#202F#5P嘿嘿，不愧是利贝尔军。\n',
            '知道该怎么样好好对待飞船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0001)
    OP_8C(0x0102, 0, 400)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020280245V#1035F#2P我知道你们很高兴，\n',
            '不过时间所剩不多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280262V#1030F启动钥匙也到手了\n',
            '能不能赶快准备出发呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x012A, 180, 400)

    ChrTalk(
        0x012A,
        (
            '#0290280247V#200F#6P是是，知道啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0129, 180, 400)
    OP_8C(0x0146, 180, 400)

    ChrTalk(
        0x0129,
        (
            '#0300280248V#198F#6P真是的……\n',
            '再让我们沉浸一下嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280265V#210F#6P那么进去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1804)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x664
@scena.Code('func_03_664')
def func_03_664():
    SetChrPos(0x00FE, -17220, 0, -8680, 180)
    ClearChrFlags(0x00FE, 0x0080)
    OP_90(0x00FE, 0, 0, -8000, 3000, 0x00)

    Return()

# id: 0x0004 offset: 0x68F
@scena.Code('func_04_68F')
def func_04_68F():
    SetChrPos(0x00FE, -17220, 0, -8680, 180)
    ClearChrFlags(0x00FE, 0x0080)
    OP_90(0x00FE, 0, 0, -6820, 3000, 0x00)

    Return()

# id: 0x0005 offset: 0x6BA
@scena.Code('func_05_6BA')
def func_05_6BA():
    SetChrPos(0x00FE, -17220, 0, -8680, 180)
    ClearChrFlags(0x00FE, 0x0080)
    OP_90(0x00FE, 0, 0, -5820, 3000, 0x00)

    Return()

# id: 0x0006 offset: 0x6E5
@scena.Code('func_06_6E5')
def func_06_6E5():
    SetChrPos(0x00FE, -17220, 0, -8680, 180)
    ClearChrFlags(0x00FE, 0x0080)
    OP_90(0x00FE, 0, 0, -4820, 3000, 0x00)

    Return()

# id: 0x0007 offset: 0x710
@scena.Code('func_07_710')
def func_07_710():
    OP_90(0x00FE, 2500, 0, 0, 3000, 0x00)
    OP_8E(0x00FE, -10500, 4000, 730, 3000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x0008 offset: 0x740
@scena.Code('func_08_740')
def func_08_740():
    OP_90(0x00FE, 0, 0, -1000, 3000, 0x00)
    OP_90(0x00FE, 2500, 0, 0, 3000, 0x00)
    OP_8E(0x00FE, -10770, 4000, -480, 3000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x0009 offset: 0x784
@scena.Code('func_09_784')
def func_09_784():
    OP_90(0x00FE, 0, 0, -2000, 3000, 0x00)
    OP_90(0x00FE, 2500, 0, 0, 3000, 0x00)
    OP_8E(0x00FE, -12060, 4000, 720, 3000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x000A offset: 0x7C8
@scena.Code('func_0A_7C8')
def func_0A_7C8():
    OP_90(0x00FE, 0, 0, -3000, 3000, 0x00)
    OP_90(0x00FE, 2500, 0, 0, 3000, 0x00)
    OP_8E(0x00FE, -11760, 4000, -1610, 3000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x000B offset: 0x80C
@scena.Code('func_0B_80C')
def func_0B_80C():
    CreateThread(0x000A, 0x00, 0x00, 0x000C)
    Sleep(300)

    CreateThread(0x000B, 0x00, 0x00, 0x000D)
    Sleep(400)

    CreateThread(0x000C, 0x00, 0x00, 0x000E)
    Sleep(300)

    CreateThread(0x000D, 0x00, 0x00, 0x000F)

    Return()

# id: 0x000C offset: 0x838
@scena.Code('func_0C_838')
def func_0C_838():
    OP_8E(0x00FE, -16520, 2000, -16600, 5000, 0x00)
    OP_8E(0x00FE, -13000, 2000, -16600, 5000, 0x00)
    OP_8E(0x00FE, -11660, 4000, -8180, 5000, 0x00)
    OP_8C(0x00FE, 0, 400)
    SetChrChipByIndex(0x00FE, 19)
    SetChrSubChip(0x00FE, 0)

    Return()

# id: 0x000D offset: 0x886
@scena.Code('func_0D_886')
def func_0D_886():
    OP_8E(0x00FE, -17490, 2000, -16600, 5000, 0x00)
    OP_8E(0x00FE, -14000, 2000, -16600, 5000, 0x00)
    OP_8E(0x00FE, -12970, 4000, -7980, 5000, 0x00)
    OP_8C(0x00FE, 0, 400)
    SetChrChipByIndex(0x00FE, 19)
    SetChrSubChip(0x00FE, 0)

    Return()

# id: 0x000E offset: 0x8D4
@scena.Code('func_0E_8D4')
def func_0E_8D4():
    OP_8E(0x00FE, -16520, 1000, -16600, 5000, 0x00)
    OP_8E(0x00FE, -13000, 1000, -16600, 5000, 0x00)
    OP_8E(0x00FE, -11430, 4000, -9840, 5000, 0x00)
    OP_8C(0x00FE, 0, 400)
    SetChrChipByIndex(0x00FE, 19)
    SetChrSubChip(0x00FE, 0)

    Return()

# id: 0x000F offset: 0x922
@scena.Code('func_0F_922')
def func_0F_922():
    OP_8E(0x00FE, -17500, 1000, -16600, 5000, 0x00)
    OP_8E(0x00FE, -14000, 1000, -16600, 5000, 0x00)
    OP_8E(0x00FE, -12970, 4000, -9610, 5000, 0x00)
    OP_8C(0x00FE, 0, 400)
    SetChrChipByIndex(0x00FE, 19)
    SetChrSubChip(0x00FE, 0)

    Return()

# id: 0x0010 offset: 0x970
@scena.Code('func_10_970')
def func_10_970():
    Call(0, 0x0011)
    Call(0, 0x0012)
    Call(0, 0x0013)

    Return()

# id: 0x0011 offset: 0x97D
@scena.Code('func_11_97D')
def func_11_97D():
    EventBegin(0x00)
    Fade(1000)
    OP_6D(-10510, 4000, 30, 0)
    OP_67(0, 5790, -10000, 0)
    OP_6B(3930, 0)
    OP_6C(145000, 0)
    OP_6E(255, 0)
    SetChrPos(0x000A, -15480, 4000, -12010, 0)
    SetChrPos(0x0102, -11480, 4000, -1700, 90)
    SetChrPos(0x0146, -12030, 4000, 580, 90)
    SetChrPos(0x0129, -10510, 4000, 720, 90)
    SetChrPos(0x012A, -10510, 4000, -1000, 90)
    OP_0D()

    NpcTalk(
        0x000A,
        '声音',
        (
            '#2450280266V#3P……走喽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0146, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0129, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x012A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000A, -16520, 2000, -11870, 0)
    SetChrPos(0x000B, -17490, 2000, -11830, 0)
    SetChrPos(0x000C, -16520, 1000, -10800, 0)
    SetChrPos(0x000D, -17500, 1000, -10870, 0)
    SetChrChipByIndex(0x000A, 16)
    SetChrChipByIndex(0x000B, 16)
    SetChrChipByIndex(0x000C, 16)
    SetChrChipByIndex(0x000D, 16)

    @scena.Lambda('lambda_0B1D')
    def lambda_0B1D():
        OP_6D(-12670, 4000, -11680, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0B1D)

    @scena.Lambda('lambda_0B35')
    def lambda_0B35():
        OP_67(0, 6070, -10000, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0B35)

    @scena.Lambda('lambda_0B4D')
    def lambda_0B4D():
        OP_6C(147000, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_0B4D)

    @scena.Lambda('lambda_0B5D')
    def lambda_0B5D():
        OP_6B(2880, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0B5D)

    @scena.Lambda('lambda_0B6D')
    def lambda_0B6D():
        OP_6E(322, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0B6D)

    CreateThread(0x000D, 0x03, 0x00, 0x000B)

    @scena.Lambda('lambda_0B84')
    def lambda_0B84():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0B84)

    Sleep(100)

    @scena.Lambda('lambda_0B97')
    def lambda_0B97():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0146, 0x0001, lambda_0B97)

    Sleep(50)

    @scena.Lambda('lambda_0BAA')
    def lambda_0BAA():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x012A, 0x0001, lambda_0BAA)

    Sleep(100)

    @scena.Lambda('lambda_0BBD')
    def lambda_0BBD():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0129, 0x0001, lambda_0BBD)

    Sleep(3000)

    OP_6D(-11430, 4000, -4670, 1500)

    ChrTalk(
        0x0129,
        (
            '#0300280267V#192F#5P哎哎……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012A,
        (
            '#0290280268V#201F#5P切，被发现了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000E, 0x0000)

    ChrTalk(
        0x000B,
        (
            '#2460280269V#4P空贼！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2450280270V#6P什，什么时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2500280271V是这些家伙让队长他们\n',
            '昏过去的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0102, 5)
    SetChrSubChip(0x0102, 0)
    OP_0D()

    ChrTalk(
        0x0102,
        (
            '#0020280272V#1032F#5P没办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x00D8, 0x00, 0x64)
    SetChrChipByIndex(0x0146, 7)
    SetChrSubChip(0x0146, 0)
    Sleep(50)

    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x012A, 11)
    SetChrSubChip(0x012A, 0)
    Sleep(50)

    OP_22(0x00D8, 0x00, 0x64)
    SetChrChipByIndex(0x0129, 9)
    SetChrSubChip(0x0129, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0146,
        (
            '#0090280273V#214F#6P就让它们乖乖地睡一觉吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0D59')
    def lambda_0D59():
        OP_6D(-11680, 4000, -4390, 500)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_0D59)

    @scena.Lambda('lambda_0D71')
    def lambda_0D71():
        OP_6B(2500, 500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0D71)

    @scena.Lambda('lambda_0D81')
    def lambda_0D81():
        OP_90(0x00FE, -500, 0, -3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0D81)

    SetChrChipByIndex(0x000A, 16)

    @scena.Lambda('lambda_0DA1')
    def lambda_0DA1():
        OP_90(0x00FE, 500, 0, 3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0DA1)

    Sleep(50)

    @scena.Lambda('lambda_0DC1')
    def lambda_0DC1():
        OP_90(0x00FE, -500, 0, -3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x012A, 0x0001, lambda_0DC1)

    SetChrChipByIndex(0x000B, 16)

    @scena.Lambda('lambda_0DE1')
    def lambda_0DE1():
        OP_90(0x00FE, 500, 0, 3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0DE1)

    Sleep(50)

    SetChrFlags(0x0146, 0x1000)
    SetChrChipByIndex(0x0146, 8)

    @scena.Lambda('lambda_0E0B')
    def lambda_0E0B():
        OP_90(0x00FE, -500, 0, -3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0146, 0x0001, lambda_0E0B)

    SetChrChipByIndex(0x000C, 16)

    @scena.Lambda('lambda_0E2B')
    def lambda_0E2B():
        OP_90(0x00FE, 500, 0, 3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0E2B)

    Sleep(50)

    @scena.Lambda('lambda_0E4B')
    def lambda_0E4B():
        OP_90(0x00FE, -500, 0, -3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0129, 0x0001, lambda_0E4B)

    SetChrChipByIndex(0x000D, 16)

    @scena.Lambda('lambda_0E6B')
    def lambda_0E6B():
        OP_90(0x00FE, 500, 0, 3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0E6B)

    Sleep(200)

    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0146, 0xFF)
    TerminateThread(0x0129, 0xFF)
    TerminateThread(0x012A, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    Battle(0x000000A6, 0x00000000, 0x00, 0x0000, 0xFF)

    Return()

# id: 0x0012 offset: 0xEB3
@scena.Code('func_12_EB3')
def func_12_EB3():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_0D()
    Sleep(1000)

    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0146, 65535)
    SetChrChipByIndex(0x0129, 65535)
    SetChrChipByIndex(0x012A, 65535)
    OP_8C(0x0102, 180, 0)
    OP_8C(0x0146, 180, 0)
    OP_8C(0x0129, 180, 0)
    OP_8C(0x012A, 180, 0)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    Call(0, 0x0021)
    SetChrPos(0x0102, -12270, 4000, -1460, 0)
    SetChrPos(0x0146, -12610, 4000, 500, 0)
    SetChrPos(0x0129, -11560, 4000, 690, 0)
    SetChrPos(0x012A, -11070, 4000, -1280, 0)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x0146, 65535)
    SetChrSubChip(0x0146, 0)
    SetChrChipByIndex(0x012A, 65535)
    SetChrSubChip(0x012A, 0)
    SetChrChipByIndex(0x0129, 65535)
    SetChrSubChip(0x0129, 0)
    OP_6D(-11090, 4000, -1010, 0)
    OP_67(0, 4860, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(147000, 0)
    OP_6E(322, 0)
    FadeIn(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0146,
        (
            '#0090280274V#210F#6P哈哈，搞定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280275V#1035F#2P一定很快还会有后援来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280276V#1030F这里由我来挡住，\n',
            '拜托你们，准备出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1059')
    def lambda_1059():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0129, 0x0001, lambda_1059)

    Sleep(50)

    @scena.Lambda('lambda_106C')
    def lambda_106C():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x012A, 0x0001, lambda_106C)

    Sleep(50)

    OP_8C(0x0146, 180, 400)

    ChrTalk(
        0x0129,
        (
            '#0300280277V#196F#6P哦哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012A,
        (
            '#0290280278V#202F#5P交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Yield()
    OP_8C(0x0129, 90, 500)

    @scena.Lambda('lambda_10D9')
    def lambda_10D9():
        OP_6D(-7230, 4000, -1520, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_10D9)

    CreateThread(0x0129, 0x01, 0x00, 0x0014)
    OP_8C(0x012A, 90, 500)
    OP_8C(0x0146, 90, 500)
    OP_8C(0x0102, 90, 500)
    Sleep(500)

    CreateThread(0x012A, 0x01, 0x00, 0x0015)
    Sleep(1000)

    OP_6D(-10160, 4000, -1430, 1500)
    OP_8C(0x0102, 0, 400)

    ChrTalk(
        0x0102,
        (
            '#0020280279V#1034F#2P乔丝特……\n',
            '你不走吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0146, 180, 400)

    ChrTalk(
        0x0146,
        (
            '#0090280280V#210F#6P发动『山猫号』\n',
            '有哥哥他们在就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090280281V我要在这里\n',
            '支援你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280282V#1032F#2P但是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280283V#211F#6P嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090280284V虽然总是装得很酷，\n',
            '不过你还是太嫩了点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280285V#1034F#2P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280286V#210F#6P就因为\n',
            '你救了我们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090280287V所以从没想过我们会\n',
            '抛弃你自己逃走吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280288V#1031F#2P……我看人的眼光\n',
            '还是挺准的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280289V特别是像你们这样\n',
            '的老好人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280290V#216F#6P你，你才是老好人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0008, 0x0080)
    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x0008, -13110, 4000, -15810, 0)

    NpcTalk(
        0x0008,
        '男人的声音',
        (
            '#0110280291V#3P哎呀呀……\n',
            '还以为是谁在吵闹呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0146, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_13FA')
    def lambda_13FA():
        OP_8C(0x00FE, 192, 500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_13FA)

    Sleep(50)

    @scena.Lambda('lambda_140D')
    def lambda_140D():
        OP_8C(0x00FE, 192, 500)

        ExitThread()

    DispatchAsync(0x0146, 0x0001, lambda_140D)

    OP_20(0x000007D0)

    @scena.Lambda('lambda_1420')
    def lambda_1420():
        OP_8E(0x00FE, -12510, 4000, -8000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1420)

    OP_6D(-11750, 4000, -5000, 2000)

    ChrTalk(
        0x0146,
        (
            '#0090280151V#213F#6P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0008, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#0110280293V#277F#2P『卡普亚空贼团』……\n',
            '竟然在这时候出现了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280294V而且没想到连你也在一起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280295V#1035F#1P……想起来了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280296V#216F#6P这，这里怎么会\n',
            '有埃雷波尼亚军人！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090280297V是你认识的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280298V#1030F#1P……见过而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280299V大概是在互不侵犯条约之前\n',
            '来接收飞船的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0110280300V#270F#2P如你所料。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280301V#272F就算这艘船被夺走，\n',
            '对我们来说也是无关紧要……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280302V不过既然碰上了，\n',
            '也不能就这么放过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    OP_6D(-12170, 4000, -6200, 0)
    OP_67(0, 3810, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(175000, 0)
    OP_6E(322, 0)
    OP_0D()
    SetChrChipByIndex(0x0008, 15)
    SetChrSubChip(0x0008, 1)
    OP_22(0x01F9, 0x00, 0x64)
    OP_99(0x0008, 0x01, 0x06, 0x000007D0)
    OP_1D(0x33)
    Sleep(500)

    WaitForThreadExit(0x0008, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0110280303V#270F#5P让我重新报上名号吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280304V我是帝国军第７机甲师团所属──\n',
            '穆拉·范德尔少校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280305V#212F#8P呜……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0102, 5)
    SetChrSubChip(0x0102, 0)
    Sleep(100)

    OP_22(0x00D8, 0x00, 0x64)
    SetChrChipByIndex(0x0146, 7)
    SetChrSubChip(0x0146, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020280306V#1032F#6P小心……\n',
            '看来这不是个容易对付的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0110280307V#272F#5P应该不及你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0110280308V#271F#5P#3S上吧！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    @scena.Lambda('lambda_1823')
    def lambda_1823():
        OP_6D(-12230, 4000, -4280, 300)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1823)

    @scena.Lambda('lambda_183B')
    def lambda_183B():
        OP_6B(2480, 300)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_183B)

    SetChrChipByIndex(0x0008, 14)
    SetChrFlags(0x0008, 0x1000)

    @scena.Lambda('lambda_1855')
    def lambda_1855():
        OP_90(0x00FE, 0, 0, 3000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1855)

    Sleep(10)

    SetChrFlags(0x0102, 0x1000)
    SetChrChipByIndex(0x0102, 6)

    @scena.Lambda('lambda_187F')
    def lambda_187F():
        OP_90(0x00FE, 0, 0, -3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_187F)

    Sleep(50)

    SetChrFlags(0x0146, 0x1000)
    SetChrSubChip(0x0146, 0)
    SetChrChipByIndex(0x0146, 8)

    @scena.Lambda('lambda_18AE')
    def lambda_18AE():
        OP_90(0x00FE, 0, 0, -3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0146, 0x0001, lambda_18AE)

    Sleep(100)

    FormationDelMember(0x28, 0xFF)
    FormationDelMember(0x29, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0146, 0xFF)
    TerminateThread(0x0008, 0xFF)
    Battle(0x000000A8, 0x00000000, 0x00, 0x0000, 0xFF)
    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    Return()

# id: 0x0013 offset: 0x190A
@scena.Code('func_13_190A')
def func_13_190A():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    Sleep(1000)

    Call(0, 0x0021)
    FormationAddMember(ChrTable['多伦'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['吉尔'], 0xFF, 0xFF)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0146, 0x01)
    TerminateThread(0x0008, 0x01)
    ClearChrFlags(0x0102, 0x1000)
    ClearChrFlags(0x0146, 0x1000)
    ClearChrFlags(0x0008, 0x1000)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0129, 0x0080)
    SetChrFlags(0x012A, 0x0080)
    Call(0, 0x0021)
    SetChrChipByIndex(0x0102, 5)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x0146, 7)
    SetChrSubChip(0x0146, 0)
    SetChrChipByIndex(0x0008, 15)
    SetChrSubChip(0x0008, 6)
    SetChrPos(0x0102, -12270, 4000, -1460, 180)
    SetChrPos(0x0146, -12610, 4000, 500, 180)
    SetChrPos(0x0008, -12510, 4000, -8000, 0)
    OP_6D(-12170, 4000, -6200, 0)
    OP_67(0, 3810, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(175000, 0)
    OP_6E(322, 0)
    OP_A3(0x0000)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_19F6'),
        (0x00000001, 'loc_19FC'),
        (-1, 'loc_1A02'),
    )

    def _loc_19F6(): pass

    label('loc_19F6')

    OP_A2(0x0000)

    Jump('loc_1A02')

    def _loc_19FC(): pass

    label('loc_19FC')

    OP_A3(0x0000)

    Jump('loc_1A02')

    def _loc_1A02(): pass

    label('loc_1A02')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A78',
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◆赢了对穆拉的战斗】\n'),
            TXT(0x01, '【◆输了对穆拉的战斗】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1A6C'),
        (0x00000001, 'loc_1A72'),
        (-1, 'loc_1A78'),
    )

    def _loc_1A6C(): pass

    label('loc_1A6C')

    OP_A2(0x0000)

    Jump('loc_1A78')

    def _loc_1A72(): pass

    label('loc_1A72')

    OP_A3(0x0000)

    Jump('loc_1A78')

    def _loc_1A78(): pass

    label('loc_1A78')

    FadeIn(1500, 0)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1AD5',
    )

    ChrTalk(
        0x0146,
        (
            '#0090280309V#214F#8P呼呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090280310V为，为什么打不倒！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B15')

    def _loc_1AD5(): pass

    label('loc_1AD5')

    ChrTalk(
        0x0146,
        (
            '#0090280311V#215F#8P呜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090280312V不行……太强了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B15(): pass

    label('loc_1B15')

    ChrTalk(
        0x0102,
        (
            '#0020280313V#1035F#6P好厉害的高手……\n',
            '而且姓范德尔吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280314V#1031F奥利维尔的真正身份，\n',
            '我大概已经猜出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0110280315V#272F#5P如果要这么说的话，\n',
            '你的真正身份也实在令人吃惊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280316V#270F『哈梅尔』的遗孤，\n',
            '约修亚·阿斯特雷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280317V#1034F#6P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0146,
        (
            '#0090280318V#213F#8P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0110280319V#276F#5P果然是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280320V那个吊儿郎当的家伙，\n',
            '直觉有时候还挺准的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280321V#1038F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'map\\\\mp056_00.eff')
    PlayEffect(0x00, 0x01, 0x0102, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0117, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0146,
        (
            '#0090280322V#216F#8P约，约修亚！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280323V#1038F#6P可以告诉我吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280324V为什么你们\n',
            '会知道那件事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0110280325V#272F#5P看来这句话让你\n',
            '认真起来了呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280326V#270F那么我也全力迎战吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x02, 'map\\\\mp057_00.eff')
    PlayEffect(0x02, 0x02, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0117, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0146, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0146,
        (
            '#0090280327V#216F#8P慢，慢着……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x01, 'map\\\\mp021_00.eff')
    CreateThread(0x012A, 0x00, 0x00, 0x001F)
    Sleep(1000)

    OP_62(0x0146, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    SetChrChipByIndex(0x0146, 65535)
    OP_8C(0x0146, 90, 400)

    @scena.Lambda('lambda_1F2B')
    def lambda_1F2B():
        OP_6D(-7530, 6580, -2230, 8000)

        ExitThread()

    DispatchAsync(0x0146, 0x0000, lambda_1F2B)

    @scena.Lambda('lambda_1F43')
    def lambda_1F43():
        OP_67(0, 6340, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0146, 0x0001, lambda_1F43)

    @scena.Lambda('lambda_1F5B')
    def lambda_1F5B():
        OP_6B(2000, 8000)

        ExitThread()

    DispatchAsync(0x0146, 0x0002, lambda_1F5B)

    @scena.Lambda('lambda_1F6B')
    def lambda_1F6B():
        OP_6E(603, 8000)

        ExitThread()

    DispatchAsync(0x0146, 0x0003, lambda_1F6B)

    @scena.Lambda('lambda_1F7B')
    def lambda_1F7B():
        OP_6C(90000, 8000)

        ExitThread()

    DispatchAsync(0x012A, 0x0001, lambda_1F7B)

    WaitForThreadExit(0x012A, 0x0000)
    OP_22(0x006A, 0x00, 0x64)
    OP_6F(0x0000, 160)
    OP_70(0x0000, 0x00000050)
    OP_73(0x0000)
    Sleep(200)

    ClearChrFlags(0x012A, 0x0080)
    SetChrFlags(0x012A, 0x0004)
    SetChrPos(0x012A, -3020, 9000, -1200, 270)
    OP_8F(0x012A, -3020, 9500, -1200, 2000, 0x00)
    OP_82(0x04, 0x02)
    WaitForThreadExit(0x0146, 0x0000)
    Sleep(500)

    ChrTalk(
        0x012A,
        (
            '#0290280328V#201F#6P准备完毕了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290280329V你们俩快跳上来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_82(0x01, 0x02)
    Sleep(300)

    OP_82(0x02, 0x02)
    Sleep(300)

    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0102, 0)
    Sleep(200)

    SetChrChipByIndex(0x0008, 0)
    SetChrSubChip(0x0008, 0)
    OP_0D()
    Sleep(300)

    OP_8C(0x0102, 90, 400)
    OP_8C(0x0008, 45, 400)

    ChrTalk(
        0x0146,
        (
            '#0090280330V#210F#5P嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    @scena.Lambda('lambda_208B')
    def lambda_208B():
        OP_8F(0x012A, -3020, 9000, -1200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x012A, 0x0001, lambda_208B)

    Fade(500)
    OP_6D(-10520, 4000, -1950, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(1720, 0)
    OP_6C(145000, 0)
    OP_6E(603, 0)
    PlayEffect(0x01, 0x04, 0x0012, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_211D')
    def lambda_211D():
        OP_8F(0x0011, -2500, 500, 2500, 200, 0x00)

        ExitThread()

    DispatchAsync(0x0129, 0x0001, lambda_211D)

    @scena.Lambda('lambda_2138')
    def lambda_2138():
        OP_8F(0x0012, -2500, 500, 2500, 200, 0x00)

        ExitThread()

    DispatchAsync(0x0129, 0x0002, lambda_2138)

    WaitForThreadExit(0x012A, 0x0001)
    OP_6F(0x0000, 80)
    OP_70(0x0000, 0x000000A0)
    OP_23(0x006A)
    OP_22(0x00E6, 0x00, 0x64)
    SetChrFlags(0x012A, 0x0080)
    Yield()
    SetChrFlags(0x0146, 0x0004)
    SetChrBattleFlags(0x0146, 0x0020)
    OP_8F(0x0146, -10910, 4000, -230, 5000, 0x00)
    OP_22(0x00A3, 0x00, 0x64)
    SetChrChipByIndex(0x0146, 22)
    SetChrSubChip(0x0146, 5)
    OP_96(0x0146, 0xFFFFE08E, 0x000014D2, 0x00000028, 0x000007D0, 0x00001388)
    SetChrChipByIndex(0x0146, 65535)
    SetChrSubChip(0x0146, 0)
    OP_22(0x00A4, 0x00, 0x64)
    ClearChrFlags(0x0146, 0x0004)
    OP_8E(0x0146, -4700, 6050, -640, 4000, 0x00)
    OP_8C(0x0146, 270, 400)

    ChrTalk(
        0x0146,
        (
            '#0090280331V#214F#3P喂！\n',
            '在干什么！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280332V#1033F#6P………呜…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_223B')
    def lambda_223B():
        OP_6D(-10520, 4000, -9000, 4000)

        ExitThread()

    DispatchAsync(0x012A, 0x0000, lambda_223B)

    CreateThread(0x0011, 0x01, 0x00, 0x001E)
    CreateThread(0x000E, 0x01, 0x00, 0x0016)
    CreateThread(0x000F, 0x01, 0x00, 0x0018)
    CreateThread(0x0010, 0x01, 0x00, 0x0019)
    CreateThread(0x0009, 0x01, 0x00, 0x001B)
    OP_8C(0x0146, 180, 400)

    @scena.Lambda('lambda_227D')
    def lambda_227D():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_227D')

    DispatchAsync2(0x0008, 0x0001, lambda_227D)

    OP_8E(0x0102, -10510, 4000, -2000, 5000, 0x00)
    SetChrFlags(0x0102, 0x0004)
    SetChrBattleFlags(0x0102, 0x0020)
    OP_22(0x00A3, 0x00, 0x64)
    SetChrChipByIndex(0x0102, 21)
    SetChrSubChip(0x0102, 5)

    @scena.Lambda('lambda_22BB')
    def lambda_22BB():
        OP_96(0x0102, 0xFFFFE2B4, 0x00001770, 0xFFFFF830, 0x000008FC, 0x00001388)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_22BB)

    WaitForThreadExit(0x0102, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0102, 0)
    ClearChrFlags(0x0102, 0x0004)
    OP_8C(0x0102, 180, 600)
    SetChrFlags(0x0102, 0x0002)
    SetChrChipByIndex(0x0102, 23)
    SetChrSubChip(0x0102, 3)
    Sleep(500)

    TerminateThread(0x012A, 0x00)
    Fade(250)
    OP_6D(-5290, 6330, -19870, 0)
    OP_67(0, 5950, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(145000, 0)
    OP_6E(466, 0)
    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x000F, 0x0001)
    WaitForThreadExit(0x0010, 0x0001)

    @scena.Lambda('lambda_2362')
    def lambda_2362():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_2362')

    DispatchAsync2(0x000E, 0x0001, lambda_2362)

    @scena.Lambda('lambda_2373')
    def lambda_2373():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_2373')

    DispatchAsync2(0x000F, 0x0001, lambda_2373)

    @scena.Lambda('lambda_2384')
    def lambda_2384():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_2384')

    DispatchAsync2(0x0010, 0x0001, lambda_2384)

    ChrTalk(
        0x000E,
        (
            '#2480280333V#6A#6P什么！？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(300)

    ChrTalk(
        0x000F,
        (
            '#2460280334V#6A#5P别，别想逃！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(300)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_23E8')
    def lambda_23E8():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_23E8')

    DispatchAsync2(0x0009, 0x0001, lambda_23E8)

    CreateThread(0x000E, 0x02, 0x00, 0x001C)
    Sleep(100)

    CreateThread(0x000F, 0x02, 0x00, 0x001C)
    Sleep(100)

    CreateThread(0x0010, 0x02, 0x00, 0x001C)
    Sleep(100)

    CreateThread(0x0009, 0x02, 0x00, 0x001D)

    ChrTalk(
        0x0009,
        (
            '#0280280335V#25A#153F#4P哇哇～！\n',
            '最佳镜头～！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1000)

    WaitForThreadExit(0x0011, 0x0001)
    OP_20(0x00000BB8)
    FadeOut(2500, 0, -1)
    OP_0D()
    OP_6D(-11550, 6400, -22050, 0)
    OP_67(0, 3700, -10000, 0)
    OP_6B(3970, 0)
    OP_6C(157000, 0)
    OP_6E(262, 0)
    TerminateThread(0x000E, 0x02)
    TerminateThread(0x000F, 0x02)
    TerminateThread(0x0010, 0x02)
    TerminateThread(0x0009, 0x02)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0146, 0x0080)
    SetChrFlags(0x0129, 0x0080)
    SetChrFlags(0x012A, 0x0080)
    Sleep(2000)

    OP_1D(0x54)
    Sleep(500)

    FadeIn(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#2480280336V可恶！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2460280337V#5P队长怎么了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2490280338V联络哈肯大门！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x000E, 1)
    SetChrChipByIndex(0x000F, 1)
    SetChrChipByIndex(0x0010, 1)
    SetChrChipByIndex(0x0009, 3)

    @scena.Lambda('lambda_255C')
    def lambda_255C():
        OP_8E(0x00FE, -10500, 4000, -37460, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_255C)

    Sleep(100)

    CreateThread(0x000E, 0x01, 0x00, 0x0017)
    Sleep(100)

    CreateThread(0x0010, 0x01, 0x00, 0x001A)
    Sleep(2000)

    @scena.Lambda('lambda_2594')
    def lambda_2594():
        OP_6D(-14870, 6400, -19960, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2594)

    @scena.Lambda('lambda_25AC')
    def lambda_25AC():
        OP_67(0, 6180, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_25AC)

    @scena.Lambda('lambda_25C4')
    def lambda_25C4():
        OP_6B(3550, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_25C4)

    OP_6E(215, 3000)
    SetMapFlags(0x02000000)

    ChrTalk(
        0x0009,
        (
            '#0280280339V#154F哎呀呀～……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280280340V刚才那个男孩子\n',
            '好像在哪里见过的样子～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0280280341V#153F哇哇，怎么回事～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280280342V#152F要，要和奈尔前辈\n',
            '商量才行……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C1305._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0014 offset: 0x26DC
@scena.Code('func_14_26DC')
def func_14_26DC():
    SetChrFlags(0x00FE, 0x0004)
    SetChrFlags(0x00FE, 0x0040)
    SetChrBattleFlags(0x00FE, 0x0020)
    OP_8C(0x00FE, 90, 0)
    Sleep(300)

    SetChrChipByIndex(0x00FE, 24)
    SetChrSubChip(0x00FE, 0)
    OP_8E(0x00FE, -10500, 4000, 880, 4000, 0x00)
    OP_22(0x00A3, 0x00, 0x64)
    SetChrSubChip(0x00FE, 2)
    OP_96(0x00FE, 0xFFFFE0C0, 0x000014D2, 0x000000C8, 0x000007D0, 0x00000FA0)
    SetChrChipByIndex(0x00FE, 65535)
    SetChrSubChip(0x00FE, 0)
    OP_22(0x00A4, 0x00, 0x64)
    ClearChrFlags(0x00FE, 0x0004)
    OP_8E(0x00FE, -5200, 6000, 1130, 3000, 0x00)
    OP_8E(0x00FE, -4420, 5550, -1650, 3000, 0x00)
    OP_8C(0x00FE, 90, 400)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 0x0000003C)
    OP_22(0x006A, 0x00, 0x64)
    Sleep(1000)

    OP_8E(0x00FE, -2790, 5550, -1730, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0015 offset: 0x27AB
@scena.Code('func_15_27AB')
def func_15_27AB():
    SetChrChipByIndex(0x00FE, 25)
    SetChrSubChip(0x00FE, 0)
    SetChrFlags(0x00FE, 0x0004)
    SetChrFlags(0x00FE, 0x0040)
    SetChrBattleFlags(0x00FE, 0x0020)
    OP_8E(0x00FE, -10540, 4000, -800, 4000, 0x00)
    OP_8C(0x00FE, 90, 0)
    OP_22(0x00A3, 0x00, 0x64)
    SetChrSubChip(0x00FE, 2)
    OP_96(0x00FE, 0xFFFFE0C0, 0x000014D2, 0x000000C8, 0x000007D0, 0x00000FA0)
    SetChrChipByIndex(0x00FE, 65535)
    SetChrSubChip(0x00FE, 0)
    OP_22(0x00A4, 0x00, 0x64)
    ClearChrFlags(0x00FE, 0x0004)
    OP_8E(0x00FE, -5270, 6000, 890, 3000, 0x00)
    OP_8E(0x00FE, -5090, 6030, 380, 3000, 0x00)
    Sleep(1500)

    OP_8E(0x00FE, -4460, 5550, -2050, 3000, 0x00)
    OP_8E(0x00FE, -2790, 5550, -1730, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)
    Sleep(200)

    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)
    OP_23(0x006A)
    OP_22(0x00E6, 0x00, 0x64)

    Return()

# id: 0x0016 offset: 0x288A
@scena.Code('func_16_288A')
def func_16_288A():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -17060, 0, -8830, 0)

    @scena.Lambda('lambda_28B1')
    def lambda_28B1():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000000C8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_28B1)

    OP_8E(0x00FE, -17100, 4000, -16840, 6000, 0x00)
    OP_8E(0x00FE, -11610, 4000, -20170, 6000, 0x00)
    ChrTurnDirection(0x00FE, 0x0011, 400)

    Return()

# id: 0x0017 offset: 0x28ED
@scena.Code('func_17_28ED')
def func_17_28ED():
    OP_8E(0x00FE, -12000, 4000, -9000, 4000, 0x00)
    def _loc_2901(): pass

    label('loc_2901')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2925',
    )

    OP_8C(0x00FE, 225, 400)
    Sleep(1000)

    OP_8C(0x00FE, 325, 400)
    Sleep(1000)

    Jump('loc_2901')

    def _loc_2925(): pass

    label('loc_2925')

    Return()

# id: 0x0018 offset: 0x2926
@scena.Code('func_18_2926')
def func_18_2926():
    Sleep(500)

    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -17060, 0, -8830, 0)

    @scena.Lambda('lambda_2952')
    def lambda_2952():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000000C8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2952)

    OP_8E(0x00FE, -17100, 4000, -16840, 6000, 0x00)
    OP_8E(0x00FE, -11840, 4000, -22520, 6000, 0x00)
    ChrTurnDirection(0x00FE, 0x0011, 400)

    Return()

# id: 0x0019 offset: 0x298E
@scena.Code('func_19_298E')
def func_19_298E():
    Sleep(800)

    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -17060, 0, -8830, 0)

    @scena.Lambda('lambda_29BA')
    def lambda_29BA():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000000C8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_29BA)

    OP_8E(0x00FE, -17100, 4000, -16840, 6000, 0x00)
    OP_8E(0x00FE, -13240, 4000, -20330, 6000, 0x00)
    ChrTurnDirection(0x00FE, 0x0011, 400)

    Return()

# id: 0x001A offset: 0x29F6
@scena.Code('func_1A_29F6')
def func_1A_29F6():
    OP_8E(0x00FE, -17100, 4000, -16840, 4000, 0x00)
    OP_8E(0x00FE, -17060, 4000, -8830, 4000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x001B offset: 0x2A24
@scena.Code('func_1B_2A24')
def func_1B_2A24():
    Sleep(1000)

    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -17060, 0, -8830, 0)

    @scena.Lambda('lambda_2A50')
    def lambda_2A50():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000000C8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2A50)

    OP_8E(0x00FE, -17100, 4000, -16840, 6000, 0x00)
    OP_8E(0x00FE, -13790, 4000, -22260, 6000, 0x00)
    ChrTurnDirection(0x00FE, 0x0011, 400)

    Return()

# id: 0x001C offset: 0x2A8C
@scena.Code('func_1C_2A8C')
def func_1C_2A8C():
    SetChrChipByIndex(0x00FE, 18)
    def _loc_2A91(): pass

    label('loc_2A91')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2ABE',
    )

    OP_99(0x00FE, 0x00, 0x04, 0x00000A28)
    OP_22(0x01F7, 0x00, 0x64)
    Sleep(500)

    OP_99(0x00FE, 0x04, 0x00, 0x00000A28)
    Sleep(500)

    Jump('loc_2A91')

    def _loc_2ABE(): pass

    label('loc_2ABE')

    Return()

# id: 0x001D offset: 0x2ABF
@scena.Code('func_1D_2ABF')
def func_1D_2ABF():
    LoadEffect(0x00, 'map\\\\mp032_00.eff')
    SetChrChipByIndex(0x00FE, 4)
    def _loc_2AD8(): pass

    label('loc_2AD8')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2B23',
    )

    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0009, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    Jump('loc_2AD8')

    def _loc_2B23(): pass

    label('loc_2B23')

    Return()

# id: 0x001E offset: 0x2B24
@scena.Code('func_1E_2B24')
def func_1E_2B24():
    @scena.Lambda('lambda_2B2A')
    def lambda_2B2A():
        OP_8F(0x00FE, -2500, 500, -2500, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2B2A)

    @scena.Lambda('lambda_2B45')
    def lambda_2B45():
        OP_8F(0x00FE, -2500, 500, -2500, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2B45)

    Sleep(500)

    @scena.Lambda('lambda_2B65')
    def lambda_2B65():
        OP_8F(0x00FE, 640, 500, -70500, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2B65)

    @scena.Lambda('lambda_2B80')
    def lambda_2B80():
        OP_8F(0x00FE, 640, 500, -70500, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2B80)

    Sleep(500)

    OP_6F(0x0000, 200)
    OP_70(0x0000, 0x000000F0)

    @scena.Lambda('lambda_2BAE')
    def lambda_2BAE():
        OP_8F(0x00FE, 640, 500, -70500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2BAE)

    @scena.Lambda('lambda_2BC9')
    def lambda_2BC9():
        OP_8F(0x00FE, 640, 500, -70500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2BC9)

    Sleep(500)

    @scena.Lambda('lambda_2BE9')
    def lambda_2BE9():
        OP_8F(0x00FE, 640, 500, -70500, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2BE9)

    @scena.Lambda('lambda_2C04')
    def lambda_2C04():
        OP_8F(0x00FE, 640, 500, -70500, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2C04)

    Sleep(500)

    @scena.Lambda('lambda_2C24')
    def lambda_2C24():
        OP_8F(0x00FE, 640, 500, -70500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2C24)

    @scena.Lambda('lambda_2C3F')
    def lambda_2C3F():
        OP_8F(0x00FE, 640, 500, -70500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2C3F)

    Sleep(500)

    @scena.Lambda('lambda_2C5F')
    def lambda_2C5F():
        OP_8F(0x00FE, 640, 500, -70500, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2C5F)

    @scena.Lambda('lambda_2C7A')
    def lambda_2C7A():
        OP_8F(0x00FE, 640, 500, -70500, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2C7A)

    Sleep(500)

    @scena.Lambda('lambda_2C9A')
    def lambda_2C9A():
        OP_8F(0x00FE, 640, 1000, -70500, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2C9A)

    @scena.Lambda('lambda_2CB5')
    def lambda_2CB5():
        OP_8F(0x00FE, 640, 1000, -70500, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2CB5)

    Sleep(500)

    @scena.Lambda('lambda_2CD5')
    def lambda_2CD5():
        OP_8F(0x00FE, 640, 1000, -70500, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2CD5)

    @scena.Lambda('lambda_2CF0')
    def lambda_2CF0():
        OP_8F(0x00FE, 640, 1000, -70500, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2CF0)

    Sleep(500)

    @scena.Lambda('lambda_2D10')
    def lambda_2D10():
        OP_8F(0x00FE, 640, 1000, -70500, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2D10)

    @scena.Lambda('lambda_2D2B')
    def lambda_2D2B():
        OP_8F(0x00FE, 640, 1000, -70500, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2D2B)

    Sleep(500)

    @scena.Lambda('lambda_2D4B')
    def lambda_2D4B():
        OP_8F(0x00FE, 640, 1000, -70500, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2D4B)

    @scena.Lambda('lambda_2D66')
    def lambda_2D66():
        OP_8F(0x00FE, 640, 1000, -70500, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2D66)

    Sleep(500)

    WaitForThreadExit(0x0011, 0x0002)
    WaitForThreadExit(0x0012, 0x0002)
    OP_24(0x0077, 0x5A)
    OP_24(0x0079, 0x5A)
    Sleep(100)

    OP_24(0x0077, 0x50)
    OP_24(0x0079, 0x50)
    Sleep(100)

    OP_24(0x0077, 0x46)
    OP_24(0x0079, 0x46)
    Sleep(100)

    OP_24(0x0077, 0x3C)
    OP_24(0x0079, 0x3C)
    Sleep(100)

    OP_24(0x0077, 0x32)
    OP_24(0x0079, 0x32)
    Sleep(100)

    OP_24(0x0077, 0x28)
    OP_24(0x0079, 0x28)
    Sleep(100)

    OP_24(0x0077, 0x1E)
    OP_24(0x0079, 0x1E)
    Sleep(100)

    OP_24(0x0077, 0x14)
    OP_24(0x0079, 0x14)
    Sleep(100)

    OP_24(0x0077, 0x0A)
    OP_24(0x0079, 0x0A)
    Sleep(100)

    OP_23(0x0077)
    OP_23(0x0079)
    OP_82(0x04, 0x00)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)

    Return()

# id: 0x001F offset: 0x2E13
@scena.Code('func_1F_2E13')
def func_1F_2E13():
    PlayEffect(0x01, 0x04, 0x0012, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0079, 0x00, 0x64)
    OP_24(0x0079, 0x46)
    Sleep(500)

    OP_24(0x0079, 0x50)
    Sleep(500)

    OP_24(0x0079, 0x5A)
    Sleep(500)

    OP_24(0x0079, 0x64)
    Sleep(500)

    SetChrFlags(0x0011, 0x0004)
    OP_22(0x0077, 0x00, 0x64)
    Sleep(500)

    OP_6F(0x0000, 160)
    OP_70(0x0000, 0x000000C8)

    @scena.Lambda('lambda_2E94')
    def lambda_2E94():
        OP_8F(0x0011, -1060, 1000, 0, 800, 0x00)

        ExitThread()

    DispatchAsync(0x0129, 0x0001, lambda_2E94)

    @scena.Lambda('lambda_2EAF')
    def lambda_2EAF():
        OP_8F(0x0012, -1060, 0, 0, 800, 0x00)

        ExitThread()

    DispatchAsync(0x0129, 0x0002, lambda_2EAF)

    WaitForThreadExit(0x0129, 0x0001)
    WaitForThreadExit(0x0129, 0x0002)
    Sleep(300)

    @scena.Lambda('lambda_2ED9')
    def lambda_2ED9():
        OP_8C(0x00FE, 315, 5)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_2ED9)

    @scena.Lambda('lambda_2EE7')
    def lambda_2EE7():
        OP_8C(0x00FE, 315, 5)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_2EE7)

    Sleep(400)

    @scena.Lambda('lambda_2EFA')
    def lambda_2EFA():
        OP_8C(0x00FE, 270, 8)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_2EFA)

    @scena.Lambda('lambda_2F08')
    def lambda_2F08():
        OP_8C(0x00FE, 270, 8)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_2F08)

    Sleep(400)

    @scena.Lambda('lambda_2F1B')
    def lambda_2F1B():
        OP_8C(0x00FE, 270, 10)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_2F1B)

    @scena.Lambda('lambda_2F29')
    def lambda_2F29():
        OP_8C(0x00FE, 270, 10)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_2F29)

    Sleep(400)

    @scena.Lambda('lambda_2F3C')
    def lambda_2F3C():
        OP_8C(0x00FE, 225, 13)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_2F3C)

    @scena.Lambda('lambda_2F4A')
    def lambda_2F4A():
        OP_8C(0x00FE, 225, 13)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_2F4A)

    Sleep(400)

    @scena.Lambda('lambda_2F5D')
    def lambda_2F5D():
        OP_8C(0x00FE, 225, 15)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_2F5D)

    @scena.Lambda('lambda_2F6B')
    def lambda_2F6B():
        OP_8C(0x00FE, 225, 15)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_2F6B)

    Sleep(400)

    @scena.Lambda('lambda_2F7E')
    def lambda_2F7E():
        OP_8C(0x00FE, 180, 18)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_2F7E)

    @scena.Lambda('lambda_2F8C')
    def lambda_2F8C():
        OP_8C(0x00FE, 180, 18)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_2F8C)

    Sleep(400)

    @scena.Lambda('lambda_2F9F')
    def lambda_2F9F():
        OP_8C(0x00FE, 180, 20)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_2F9F)

    @scena.Lambda('lambda_2FAD')
    def lambda_2FAD():
        OP_8C(0x00FE, 180, 20)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_2FAD)

    Sleep(400)

    @scena.Lambda('lambda_2FC0')
    def lambda_2FC0():
        OP_8C(0x00FE, 180, 23)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_2FC0)

    @scena.Lambda('lambda_2FCE')
    def lambda_2FCE():
        OP_8C(0x00FE, 180, 23)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_2FCE)

    Sleep(400)

    @scena.Lambda('lambda_2FE1')
    def lambda_2FE1():
        OP_8C(0x00FE, 180, 25)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_2FE1)

    @scena.Lambda('lambda_2FEF')
    def lambda_2FEF():
        OP_8C(0x00FE, 180, 25)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_2FEF)

    Sleep(400)

    @scena.Lambda('lambda_3002')
    def lambda_3002():
        OP_8C(0x00FE, 180, 28)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_3002)

    @scena.Lambda('lambda_3010')
    def lambda_3010():
        OP_8C(0x00FE, 180, 28)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_3010)

    Sleep(3000)

    @scena.Lambda('lambda_3023')
    def lambda_3023():
        OP_8F(0x0011, -2500, 0, 2500, 700, 0x00)

        ExitThread()

    DispatchAsync(0x0129, 0x0001, lambda_3023)

    @scena.Lambda('lambda_303E')
    def lambda_303E():
        OP_8F(0x0012, -2500, 0, 2500, 700, 0x00)

        ExitThread()

    DispatchAsync(0x0129, 0x0002, lambda_303E)

    @scena.Lambda('lambda_3059')
    def lambda_3059():
        OP_8C(0x00FE, 180, 25)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_3059)

    @scena.Lambda('lambda_3067')
    def lambda_3067():
        OP_8C(0x00FE, 180, 25)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_3067)

    Sleep(400)

    @scena.Lambda('lambda_307A')
    def lambda_307A():
        OP_8C(0x00FE, 180, 23)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_307A)

    @scena.Lambda('lambda_3088')
    def lambda_3088():
        OP_8C(0x00FE, 180, 23)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_3088)

    Sleep(400)

    @scena.Lambda('lambda_309B')
    def lambda_309B():
        OP_8C(0x00FE, 180, 18)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_309B)

    @scena.Lambda('lambda_30A9')
    def lambda_30A9():
        OP_8C(0x00FE, 180, 18)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_30A9)

    Sleep(400)

    @scena.Lambda('lambda_30BC')
    def lambda_30BC():
        OP_8C(0x00FE, 180, 10)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_30BC)

    @scena.Lambda('lambda_30CA')
    def lambda_30CA():
        OP_8C(0x00FE, 180, 10)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_30CA)

    Sleep(400)

    @scena.Lambda('lambda_30DD')
    def lambda_30DD():
        OP_8C(0x00FE, 180, 8)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_30DD)

    @scena.Lambda('lambda_30EB')
    def lambda_30EB():
        OP_8C(0x00FE, 180, 8)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_30EB)

    Sleep(400)

    WaitForThreadExit(0x0011, 0x0003)
    WaitForThreadExit(0x0129, 0x0001)
    WaitForThreadExit(0x0129, 0x0002)
    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    Sleep(500)

    Return()

# id: 0x0020 offset: 0x3123
@scena.Code('func_20_3123')
def func_20_3123():
    SetChrChipByIndex(0x0008, 0)
    OP_8E(0x00FE, -13660, 4000, -16000, 3000, 0x00)
    OP_8E(0x00FE, -16820, 4000, -16920, 3000, 0x00)
    OP_8E(0x00FE, -16970, 0, -9160, 3000, 0x00)

    Return()

# id: 0x0021 offset: 0x3165
@scena.Code('func_21_3165')
def func_21_3165():
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000A, 0x0001)
    ClearChrFlags(0x000B, 0x0001)
    ClearChrFlags(0x000C, 0x0001)
    ClearChrFlags(0x000D, 0x0001)
    SetChrChipByIndex(0x000A, 17)
    SetChrChipByIndex(0x000B, 17)
    SetChrChipByIndex(0x000C, 17)
    SetChrChipByIndex(0x000D, 17)
    SetChrSubChip(0x000A, 0)
    SetChrSubChip(0x000B, 0)
    SetChrSubChip(0x000C, 0)
    SetChrSubChip(0x000D, 0)
    SetChrPos(0x000A, -11960, 4000, 4040, 315)
    SetChrPos(0x000B, -12210, 4000, 6160, 90)
    SetChrPos(0x000C, -13650, 4000, 6030, 180)
    SetChrPos(0x000D, -13510, 4000, 3710, 45)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
