import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C0403_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0403   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '阿加特'),
    TXT(0x02, '金'),
    TXT(0x03, '幽灵骸骨鱼'),
    TXT(0x04, '亚鲁瓦教授'),
    TXT(0x05, '约修亚'),
    TXT(0x06, '奈尔'),
    TXT(0x07, '朵洛希'),
    TXT(0x08, '目标用摄像机'),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 16
    header.bgm            = 33
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x403C
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
            word_32         = 45,
            word_34         = 45,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 16,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0xFFFFF448,
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
            word_32         = 45,
            word_34         = 45,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 16,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xEC
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH00390._CH', 'ED6_DT07/CH00390P._CP'),
        ('ED6_DT07/CH00391._CH', 'ED6_DT07/CH00391P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT09/CH10090._CH', 'ED6_DT09/CH10090P._CP'),
        ('ED6_DT09/CH10091._CH', 'ED6_DT09/CH10091P._CP'),
        ('ED6_DT07/CH02050._CH', 'ED6_DT07/CH02050P._CP'),
        ('ED6_DT07/CH00010._CH', 'ED6_DT07/CH00010P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT06/CH20063._CH', 'ED6_DT06/CH20063P._CP'),
        ('ED6_DT06/CH20064._CH', 'ED6_DT06/CH20064P._CP'),
    ]

# id: 0x10002 offset: 0x146
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 4830,
            z                   = 250,
            y                   = 7810,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 5488,
            z                   = 0,
            y                   = 16806,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 5488,
            z                   = 0,
            y                   = 16806,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 5488,
            z                   = 0,
            y                   = 16806,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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

# id: 0x10003 offset: 0x246
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x246
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 1600,
            y           = 1000,
            z           = -2680,
            range       = -1600,
            dword_10    = 0xFFFFF830,
            dword_14    = 0xFFFFE82C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000010,
        ),
    )

# id: 0x10005 offset: 0x266
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x266
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 5, 0x255)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 4, 0x254)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_27E',
    )

    EventBegin(0x00)
    OP_28(0x0019, 0x01, 0x0080)
    Event(0, 0x0008)

    def _loc_27E(): pass

    label('loc_27E')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_28A'),
        (-1, 'loc_308'),
    )

    def _loc_28A(): pass

    label('loc_28A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0043, 6, 0x21E)),
            Expr.Return,
        ),
        'loc_305',
    )

    EventBegin(0x00)
    SetMapFlags(0x00400000)
    ClearMapFlags(0x00000001)
    SetChrFlags(0x0106, 0x0008)
    SetChrFlags(0x0108, 0x0008)
    ClearChrFlags(0x0008, 0x0008)
    ClearChrFlags(0x0009, 0x0008)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0008, -1000, 0, -1600, 0)
    SetChrPos(0x0009, 500, 0, -2620, 0)
    SetChrChipByIndex(0x0008, 1)
    SetChrChipByIndex(0x0009, 3)
    CameraMove(0, 0, -10700, 0)
    OP_6C(45000, 0)
    Event(0, 0x0011)

    def _loc_305(): pass

    label('loc_305')

    Jump('loc_308')

    def _loc_308(): pass

    label('loc_308')

    Return()

# id: 0x0001 offset: 0x309
@scena.Code('Init')
def Init():
    PlaySE(451, 0x01, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 5, 0x255)),
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_323',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_323(): pass

    label('loc_323')

    Return()

# id: 0x0002 offset: 0x324
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0000,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_349',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_48B')

    def _loc_349(): pass

    label('loc_349')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_362',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_48B')

    def _loc_362(): pass

    label('loc_362')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37B',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_48B')

    def _loc_37B(): pass

    label('loc_37B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_394',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_48B')

    def _loc_394(): pass

    label('loc_394')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3AD',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_48B')

    def _loc_3AD(): pass

    label('loc_3AD')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C6',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_48B')

    def _loc_3C6(): pass

    label('loc_3C6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DF',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_48B')

    def _loc_3DF(): pass

    label('loc_3DF')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F8',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_48B')

    def _loc_3F8(): pass

    label('loc_3F8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_411',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_48B')

    def _loc_411(): pass

    label('loc_411')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42A',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_48B')

    def _loc_42A(): pass

    label('loc_42A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_443',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_48B')

    def _loc_443(): pass

    label('loc_443')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_45C',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_48B')

    def _loc_45C(): pass

    label('loc_45C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_475',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_48B')

    def _loc_475(): pass

    label('loc_475')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_48B',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_48B(): pass

    label('loc_48B')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4A0',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_48B')

    def _loc_4A0(): pass

    label('loc_4A0')

    Return()

# id: 0x0003 offset: 0x4A1
@scena.Code('func_03_4A1')
def func_03_4A1():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 0, 0x258)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A6B',
    )

    EventBegin(0x00)
    ClearMapFlags(0x00000001)

    ExecExpressionWithValue(
        0x000F,
        0x01,
        (
            (Expr.GetChrWork, 0xB, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x02,
        (
            (Expr.GetChrWork, 0xB, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x03,
        (
            (Expr.GetChrWork, 0xB, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000F, 800)
    SetScenaFlags(ScenaFlag(0x004B, 0, 0x258))

    ChrTalk(
        0x000B,
        (
            '#0150010790V#130F哎呀……\n',
            '你是叫艾丝蒂尔吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010791V#130F你的同伴怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010792V#000F嗯……\n',
            '他想稍微吹一会儿风。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010793V#130F这样啊。\n',
            '这里的风吹起来也挺舒服的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010794V#130F说起来，你们俩这么年轻就当上游击士，\n',
            '的确是让人佩服不已啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010795V#130F我记得要取得游击士资格，\n',
            '至少要１６岁的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010796V#001F嘿～知道得很清楚嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010797V#001F嗯。\n',
            '我们正好１６岁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010798V#130F年轻真是好啊。\n',
            '只要年轻就有无限的可能性。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010799V#130F如果我也能年轻个１０岁，\n',
            '就能亲自去解开沉眠于\n',
            '整个大陆上的古代遗迹之谜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010800V#000F整个大陆很广阔吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010801V#000F这么说，\n',
            '教授不是利贝尔人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010802V#130F嗯，我是北方人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010803V#130F啊……\n',
            '不过不是埃雷波尼亚出身哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010804V#001F啊哈哈，不用担心啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010805V#003F我虽然十分讨厌战争……\n',
            '不过这并不代表我痛恨帝国的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010806V#130F……难道你重要的人被……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010807V#500F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010808V#000F嗯……我的母亲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010809V#131F实在抱歉……\n',
            '问了些不该问的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010810V#000F没什么，不用介意。\n',
            '这已经是十年前的事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010811V#000F在那之后我和老爸也有了新的家人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010812V#130F原来如此。\n',
            '就是那个和你在一起的同伴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010813V#001F嘿嘿，就像弟弟一样呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010814V#001F不过对约修亚来说，\n',
            '他一直都是当自己是哥哥呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010815V#132F呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010816V#008F哎呀，\n',
            '我都说了些什么啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010817V#008F这些话怎么好意思对别人说呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010818V#130F这有什么关系。\n',
            '你们能这么亲密不是很好吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_DAF')

    def _loc_A6B(): pass

    label('loc_A6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D3D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    EventBegin(0x00)
    ClearMapFlags(0x00000001)

    ExecExpressionWithValue(
        0x000F,
        0x01,
        (
            (Expr.GetChrWork, 0xB, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x02,
        (
            (Expr.GetChrWork, 0xB, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x03,
        (
            (Expr.GetChrWork, 0xB, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000F, 800)

    ChrTalk(
        0x0101,
        (
            '#0010010819V#000F对了教授……\n',
            '关于这座塔，你又弄清了些什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010820V#130F不，现在还完全摸不着头脑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010821V#130F看起来有必要和\n',
            '其它的塔做一下对比调查了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010822V#505F其它的塔……\n',
            '是指洛连特以外的三座塔吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010823V#130F嗯，正是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010824V#130F柏斯地区的『琥珀之塔』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010825V#130F卢安地区的『绀碧之塔』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010826V#130F蔡斯地区的『红莲之塔』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010827V#130F每座塔都是和这座『翡翠之塔』\n',
            '同一时代建造的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010828V#001F果然了解得很清楚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010829V#006F不过，调查虽然很有趣……\n',
            '可不要做太危险的事情哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010830V虽然要花点钱，\n',
            '不过还是请个游击士做护卫比较好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010831V#130F哈哈，我可是个贫穷学者……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_DAF')

    def _loc_D3D(): pass

    label('loc_D3D')

    ChrTalk(
        0x000B,
        (
            '#0150010832V#130F看起来这个装置的机能\n',
            '已经完全停止了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010833V#130F如果找到什么线索，\n',
            '也许可以再次启动这个装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DAF(): pass

    label('loc_DAF')

    TalkEnd(0x000B)

    Return()

# id: 0x0004 offset: 0xDB3
@scena.Code('func_04_DB3')
def func_04_DB3():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 6, 0x256)),
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 7, 0x257)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 0, 0x258)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_111B',
    )

    EventBegin(0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000B, 0xFF)
    Fade(1000)
    CameraMove(-12280, 250, 14520, 0)
    SetChrPos(0x000D, -9000, 0, 4732, 0)
    SetChrPos(0x000E, -6000, 0, 8006, 0)
    SetChrPos(0x000B, -2610, 0, 10050, 0)
    SetChrPos(0x0101, -13260, 250, 12860, 0)
    SetChrPos(0x000C, -12660, 250, 14050, 180)

    ExecExpressionWithValue(
        0x000F,
        0x01,
        (
            (Expr.GetChrWork, 0xC, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x02,
        (
            (Expr.GetChrWork, 0xC, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x03,
        (
            (Expr.GetChrWork, 0xC, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010010838V#002F约修亚，还是不舒服吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020010839V#010F#1P不，已经好多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010840V#010F应该可以正常走动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010841V#000F太好了……\n',
            '到底是什么原因呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010842V#000F如果是因为缺氧的话，\n',
            '为什么我们又没有事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010843V#001F一定是突发性的恐高症吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020010844V#019F#1P我、我想不是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0280010845V#151F小艾，小约！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000E, 400)
    ChrTurnDirection(0x000C, 0x000E, 400)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000B, 0xFF)
    CreateThread(0x000E, 0x01, 0x00, 0x0005)
    Sleep(800)

    CreateThread(0x000D, 0x01, 0x00, 0x0005)
    Sleep(1300)

    CreateThread(0x000B, 0x01, 0x00, 0x0005)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010010846V#004F啊，拍摄已经结束了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '#0280010847V#151F#1P当然啦！\n',
            '还拍了好多张呢⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0270010848V#141F#3P这样取材工作就结束了，\n',
            '我们回城里去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010849V#141F两位新人，回去的时候也拜托了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010850V#130F#1P请多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    FormationAddMember(0x01, 0xFF)
    NewScene('ED6_DT01/T0100._SN', 2, 0, 0)
    IdleLoop()

    Jump('loc_11C1')

    def _loc_111B(): pass

    label('loc_111B')

    ChrTalk(
        0x0101,
        (
            '#0010010834V#000F约修亚，好点了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020010835V#010F嗯，好了一点点吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010836V#010F已经休息了一阵子，\n',
            '#010F艾丝蒂尔你还是继续参观吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010837V#000F嗯，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11C1(): pass

    label('loc_11C1')

    TalkEnd(0x000C)

    Return()

# id: 0x0005 offset: 0x11C5
@scena.Code('func_05_11C5')
def func_05_11C5():
    OP_92(0x00FE, 0x000F, 3000, 3000, 0x00)

    Return()

# id: 0x0006 offset: 0x11D4
@scena.Code('func_06_11D4')
def func_06_11D4():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 6, 0x256)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1754',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x004A, 6, 0x256))
    ClearMapFlags(0x00000001)

    ExecExpressionWithValue(
        0x000F,
        0x01,
        (
            (Expr.GetChrWork, 0xD, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x02,
        (
            (Expr.GetChrWork, 0xD, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x03,
        (
            (Expr.GetChrWork, 0xD, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000F, 800)

    ChrTalk(
        0x000D,
        (
            '#0270010731V#145F哈～香烟的味道真好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010732V#141F来到洛连特这种乡下地方取材，\n',
            '刚开始真是一点干劲都没有……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010733V#141F不过看样子，偶尔来一次也不错嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010734V#009F哼，真是没礼貌。\n',
            '不想来的话就不要来嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0270010735V#142F这可是总编的命令啊。\n',
            '而且还得带一下那个脱线的丫头。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010736V#142F若不是这样，\n',
            '我现在应该正为了寻找独家新闻，\n',
            '而在王国全境到处奔走的旅途中呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010737V#006F哼，说是独家新闻，\n',
            '其实就是点小道消息吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0270010738V#141F我倒不讨厌小道消息，\n',
            '不过绝大部分还是正规报道啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010739V#141F……所以说，\n',
            '现在我最感兴趣的地方就是柏斯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010740V#004F柏斯地区？\n',
            '难道发生什么事情了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0270010741V#140F接连发生了大规模的盗窃案件呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010742V#140F犯人的真实身份还没有弄清，\n',
            '不过似乎是有专用交通工具的人干的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010743V#002F交通工具……是指飞艇吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010744V#002F难道说，是空贼？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0270010745V#140F这种可能性很高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010746V#140F不过，也有可能是\n',
            '埃雷波尼亚帝国策划的伪装活动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010010747V#004F啊……怎么会！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010748V#004F明明已经签订了和平条约了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0270010749V#140F的确，在十年前的战争中\n',
            '帝国也受到了重创。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010750V#140F目前在大陆诸国的监视下，\n',
            '他们应该不敢轻举妄动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010751V#140F但暗地里捣乱的可能性还是有的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010752V#003F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0270010753V#141F现在真相还隐藏在黑暗中啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010754V#141F所以说，弄清楚事实真相也是\n',
            '我们这些笔杆子的工作啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_1976')

    def _loc_1754(): pass

    label('loc_1754')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18BA',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    EventBegin(0x00)
    ClearMapFlags(0x00000001)

    ExecExpressionWithValue(
        0x000F,
        0x01,
        (
            (Expr.GetChrWork, 0xD, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x02,
        (
            (Expr.GetChrWork, 0xD, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x03,
        (
            (Expr.GetChrWork, 0xD, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000F, 800)

    ChrTalk(
        0x000D,
        (
            '#0270010755V#145F此外，\n',
            '王国军方面也有很多新动向。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010756V#145F真是的，\n',
            '有几个分身都不够用啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010757V#002F新动向？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0270010758V#140F新人军官中出现了个特别能干的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010759V#140F听说给缺乏人才而又老化的\n',
            '王国军带来了新鲜血液。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010760V#140F真想采访一下啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_1976')

    def _loc_18BA(): pass

    label('loc_18BA')

    ChrTalk(
        0x000D,
        (
            '#0270010761V#141F哈哈，即使是工作再忙碌，\n',
            '也得偷空抽一两口美味香烟啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010762V#141F最近王都的禁烟活动搞得很厉害，\n',
            '我都不敢在杂志社里面抽烟了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010763V#147F烟这种东西，果然还是戒不了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1976(): pass

    label('loc_1976')

    TalkEnd(0x000D)

    Return()

# id: 0x0007 offset: 0x197A
@scena.Code('func_07_197A')
def func_07_197A():
    TalkBegin(0x000E)
    SetChrChipByIndex(0x000E, 9)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 7, 0x257)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D07',
    )

    EventBegin(0x00)
    ClearMapFlags(0x00000001)

    ExecExpressionWithValue(
        0x000F,
        0x01,
        (
            (Expr.GetChrWork, 0xE, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x02,
        (
            (Expr.GetChrWork, 0xE, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x03,
        (
            (Expr.GetChrWork, 0xE, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000F, 800)
    SetScenaFlags(ScenaFlag(0x004A, 7, 0x257))

    ChrTalk(
        0x000E,
        (
            '#0280010764V#151F啊，小艾。\n',
            '这儿真是棒得不得了啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010765V#151F我还担心感光结晶回路\n',
            '够不够用呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010766V#000F这儿的确实风景很好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010767V#000F对了，感光结晶回路是什么东西啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0280010768V#150F是用七耀石加工出来的\n',
            '一种非常薄的结晶回路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010769V#150F是一种受到光的照射之后，\n',
            '就可以拍出照片来的装置呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010770V#004F不愧是专业摄影师，\n',
            '对自己的谋生工具很精通啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0280010771V#151F嘿嘿㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010772V#153F对了对了……\n',
            '小约他怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010773V#000F嗯……\n',
            '他想自己吹一会儿风。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0280010774V#150F哦～\n',
            '伫立在风中的黑发少年……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '#0280010775V#151F哇，应该可以拍出很好的照片呢㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010776V#151F要不要也给他拍上一张呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010777V#008F啊～\n',
            '约修亚好像不太喜欢这个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010778V#008F我想他大概会拒绝吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0280010779V#154F唔，有点可惜呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010780V#151F这样说来，\n',
            '小约还真的有点腼腆呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_1EF2')

    def _loc_1D07(): pass

    label('loc_1D07')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1ECE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    EventBegin(0x00)
    ClearMapFlags(0x00000001)

    ExecExpressionWithValue(
        0x000F,
        0x01,
        (
            (Expr.GetChrWork, 0xE, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x02,
        (
            (Expr.GetChrWork, 0xE, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x03,
        (
            (Expr.GetChrWork, 0xE, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000F, 800)

    ChrTalk(
        0x000E,
        (
            '#0280010781V#151F对了，小约不肯的话，\n',
            '小艾你来怎么样？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010782V#151F让姐姐拍一张行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010783V#004F我、我吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010784V#004F为什么要拍我呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0280010785V#151F你很可爱嘛，\n',
            '而且还有一股闪闪生辉的灵气呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010786V#151F说不定还能当封面模特哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010010787V#008F还、还是算了吧！\n',
            '怎么想也不合我的形象啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0280010788V#154F唉，又被拒绝了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_1EF2')

    def _loc_1ECE(): pass

    label('loc_1ECE')

    ChrTalk(
        0x000E,
        (
            '#0280010789V#151F唔～要拍什么好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EF2(): pass

    label('loc_1EF2')

    TalkEnd(0x000E)

    Return()

# id: 0x0008 offset: 0x1EF6
@scena.Code('func_08_1EF6')
def func_08_1EF6():
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x004A, 5, 0x255))
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    SetChrFlags(0x000C, 0x0040)
    SetChrFlags(0x000D, 0x0040)
    SetChrFlags(0x000E, 0x0040)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x0101, 90, 0, -4010, 0)
    SetChrPos(0x000C, 90, 0, -4010, 0)
    SetChrPos(0x000D, 90, 0, -4010, 0)
    SetChrPos(0x000E, 90, 0, -4010, 0)
    FormationDelMember(0x0F, 0xFF)
    FormationDelMember(0x01, 0xFF)
    FormationDelMember(0x0E, 0xFF)
    CameraMove(-2600, 0, 20370, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(5300, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_1FC3')
    def lambda_1FC3():
        CameraMove(-60, 0, 2490, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1FC3)

    @scena.Lambda('lambda_1FDB')
    def lambda_1FDB():
        ChrWalkTo(0x00FE, -40, 0, 4550, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_1FDB)

    Sleep(500)

    @scena.Lambda('lambda_1FFB')
    def lambda_1FFB():
        ChrWalkTo(0x00FE, 1020, 0, 3720, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1FFB)

    Sleep(500)

    @scena.Lambda('lambda_201B')
    def lambda_201B():
        ChrWalkTo(0x00FE, -1290, 0, 3220, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_201B)

    Sleep(500)

    @scena.Lambda('lambda_203B')
    def lambda_203B():
        ChrWalkTo(0x00FE, -20, 0, 2490, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_203B)

    Sleep(3500)

    Fade(1000)
    CameraMove(90, 0, 3680, 0)
    CameraSetDistance(3700, 0)
    SetChrDirection(0x0101, 90, 0)
    SetChrDirection(0x000C, 90, 0)
    SetChrDirection(0x000D, 315, 0)
    SetChrDirection(0x000E, 270, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010010625V#000F好耀眼啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010626V#000F终于到达塔顶了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '#0280010627V#151F哇～好美丽的景色哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0270010628V#147F呵呵，果然十分壮观。\n',
            '这样可以拍到比预想还好的照片了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000D, 0, 400)
    Sleep(300)

    ChrTalk(
        0x000D,
        (
            '#0270010629V#141F还有，那个就是我们要找的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 0, 400)
    SetChrDirection(0x000C, 0, 400)
    SetChrDirection(0x000E, 0, 400)

    @scena.Lambda('lambda_21AB')
    def lambda_21AB():
        CameraMove(430, 950, 12060, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_21AB)

    @scena.Lambda('lambda_21C3')
    def lambda_21C3():
        OP_67(0, 5170, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_21C3)

    @scena.Lambda('lambda_21DB')
    def lambda_21DB():
        CameraSetDistance(4840, 3000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_21DB)

    Sleep(3000)

    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010010630V#004F#1P那个？是什么东西啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0280010631V#151F#1P看起来像一个超级大锅，\n',
            '应该是导力器之类的东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0270010632V#141F#1P根据资料记载，\n',
            '好像是古代的装置。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010633V#141F目前还不清楚它的作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010634V#000F#1P哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_22F0')
    def lambda_22F0():
        CameraMove(90, 0, 3680, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_22F0)

    @scena.Lambda('lambda_2308')
    def lambda_2308():
        OP_67(0, 6500, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_2308)

    @scena.Lambda('lambda_2320')
    def lambda_2320():
        CameraSetDistance(3700, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_2320)

    Sleep(1500)

    ChrTurnDirection(0x0101, 0x000C, 400)

    ChrTalk(
        0x0101,
        (
            '#0010010635V#501F喂，约修亚。\n',
            '你知道这东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020010636V#015F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(500)

    ChrTurnDirection(0x000D, 0x000C, 400)
    ChrTurnDirection(0x000E, 0x000C, 400)

    ChrTalk(
        0x0101,
        (
            '#0010010637V#002F约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000C, 45, 400)
    CameraMove(2710, 250, 5470, 1000)

    ChrTalk(
        0x000C,
        (
            '#0020010638V#510F……藏起来也没用的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010639V#510F为了安全着想还是现身比较好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010640V#004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000B,
        '男性的声音',
        (
            '#0150010641V啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000B,
        '男性的声音',
        (
            '#0150010642V我、我出来！\n',
            '现在立刻就出来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    CreateThread(0x000B, 0x01, 0x00, 0x000D)
    OP_62(0x000B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x000B, 3490, 250, 8280, 3000, 0x00)
    SetChrDirection(0x000B, 225, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(200)

    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(200)

    OP_62(0x000E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010010643V#004F这、这个人是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0270010644V#143F怎么回事，有人捷足先登吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0280010645V#153F呜哇，吓了一跳～\n',
            '小约，你的感觉真敏锐呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020010646V#014F#4P……你是…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000B,
        '戴眼镜的男性',
        (
            '#0150010647V#131F抱歉，对不起！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010648V#131F我把身上的钱全都给你们，\n',
            '请饶我一命吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010010649V#007F等等，大叔……\n',
            '你怎么能把我们当成强盗啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010650V看见这个纹章就应该知道了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔展示了游击士协会的纹章。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    NpcTalk(
        0x000B,
        '戴眼镜的男性',
        (
            '#0150010651V#130F哦哦，那个是游击士协会的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010652V#130F难道……\n',
            '你们是游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010653V#006F嘿嘿，说对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010654V#006F我叫艾丝蒂尔，\n',
            '这个男孩叫约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0270010655V#141F而我们是《利贝尔通讯》的记者。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010656V#141F为了来这座塔取材，\n',
            '委托这两个游击士当护卫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2818')
    def lambda_2818():
        CameraMove(380, 0, 5840, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2818)

    ChrWalkTo(0x000B, 30, 0, 7000, 3000, 0x00)
    SetChrDirection(0x000B, 180, 400)

    NpcTalk(
        0x000B,
        '戴眼镜的男性',
        (
            '#0150010657V#131F唉～～\n',
            '真是的，不要吓我嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010658V#131F竟然来这种地方，\n',
            '不会让人觉得很可疑吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020010659V#018F这么说的话，\n',
            '你不也很可疑吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010660V#018F你到底是什么人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010661V#130F抱歉，还没做自我介绍。\n',
            '我叫亚鲁瓦，是一个考古学家。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010662V#130F为了研究古代文明\n',
            '而到这座塔做一些考古调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0280010663V#153F只有一个人？\n',
            '能平安无事到这儿还真不简单呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010664V#130F哪里，哈哈哈。\n',
            '因为调查遗迹习惯了嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010665V#130F对于从魔兽身边逃走的脚力，\n',
            '我还是很有自信的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010666V#130F……不过话说回来，\n',
            '这次还真是险些丧命呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010667V#008F真、真是一个蛮干的学者啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0270010668V#140F不过，你既然是考古学者，\n',
            '应该对这座塔的由来很清楚吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010669V#130F嗯，比起一般人应该……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010670V#130F不过刚开始调查不久，\n',
            '不清楚的地方也还不少啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0270010671V#141F这样也可以啦。\n',
            '有没有什么有趣的资料？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010672V#141F拿来给我当报道的题材也好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010673V#130F嗯，这样吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x000B)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0150010674V#130F不知道各位听说过\n',
            '『七至宝』这个词吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010675V#004F听起来，\n',
            '教区长好像告诉过我们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020010676V#012F是指女神授予古代人的，\n',
            '蕴藏巨大力量的『七至宝』吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010677V#130F嗯，就是那个！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010678V#130F传说他们凭借这些至宝的力量，\n',
            '支配了海洋、大地和天空。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010679V#130F甚至还传说他们连\n',
            '生命和时间的秘密也解开了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010680V#130F大概在１２００年前，\n',
            '一场神秘的灾难毁灭了古代文明，\n',
            '『七至宝』也因此失传了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0270010681V#140F这是在七耀教会的圣典里\n',
            '也有记载的传说啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010682V#140F那么，和这座塔有什么关系呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010683V#130F传说七至宝其中之一，\n',
            '就在这利贝尔的某处沉眠着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010684V#132F——它的名字是『辉之环』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010685V#501F『辉之环』……\n',
            '听起来很不可思议的词语啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010686V#130F如果这个传说是真的，\n',
            '我猜想作为利贝尔最古老遗迹的这座塔，\n',
            '一定留有什么线索才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010687V#130F所以我才会来这里调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0280010688V#151F哈～真是梦幻般的故事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010689V#130F呵呵……对吧！？\n',
            '是不是有种古代传承的感觉呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010690V#130F呀～！有人能理解我的研究，\n',
            '真令人感到欣慰啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020010691V#012F那样的话……\n',
            '找到什么线索了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#0150010692V#131F现、现在还没……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010693V#131F如果能解开那边的装置之谜的话，\n',
            '应该可以知道些什么吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0270010694V#145F虽然听起来很有趣，\n',
            '不过也只是推测的程度而已啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010695V#145F抱歉，你告诉我的这些资料\n',
            '作为报道还是有些欠缺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010696V#131F是吗……那太可惜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000B, 0xFF)
    ChrTurnDirection(0x0101, 0x000D, 400)

    ChrTalk(
        0x0101,
        (
            '#0010010697V#006F嘿嘿～真意外。\n',
            '你写报道出乎意料地认真啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '#0270010698V#141F#5P把来源不实的消息\n',
            '写成报道是绝对不行的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010699V#141F宁可登载小道消息也不登载无稽之谈，\n',
            '这就是《利贝尔通讯》的原则。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010700V#141F算了，按照预定计划行事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    ChrTurnDirection(0x000D, 0x000E, 400)
    ChrTurnDirection(0x0101, 0x000E, 400)
    OP_21()
    PlayBGM(1)

    ChrTalk(
        0x000D,
        (
            '#0270010701V#140F#5P朵洛希。\n',
            '拍几张洛连特全景的照片。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010702V#140F其余的就随你喜欢来拍吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010703V#140F到处都转一遍，\n',
            '尽情地多拍些好照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x000D, 400)
    OP_62(0x000E, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '#0280010704V#151F知道了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010705V#151F不肖弟子朵洛希·海娅特，\n',
            '一定会尽力拍出最好的照片！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    CreateThread(0x000E, 0x01, 0x00, 0x000D)
    SetChrDirection(0x000E, 270, 400)
    ChrWalkTo(0x000E, -3870, 250, 3420, 5000, 0x00)
    ChrWalkTo(0x000E, -8940, 250, 300, 5000, 0x00)
    TerminateThread(0x000E, 0xFF)
    Sleep(1000)

    ChrTurnDirection(0x000D, 0x000B, 400)
    ChrTurnDirection(0x000C, 0x000B, 400)
    ChrTurnDirection(0x0101, 0x000B, 400)
    ChrTurnDirection(0x000B, 0x000D, 400)

    ChrTalk(
        0x000D,
        (
            '#0270010706V#141F学者先生，难得这么巧，\n',
            '不如就和我们一起回城吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010707V#141F这两个家伙，虽然看起来只是小鬼，\n',
            '不过护卫本领还是很不赖的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010708V#009F真是话中有话呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150010709V#130F哈哈，如果能一起回去的话，\n',
            '我可求之不得啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0270010710V#141F那就这么决定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010711V#141F好了，在摄影结束之前，\n',
            '我们就稍微休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000B, 0xFF)
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_69(0x000F, 800)
    SetChrPos(0x0101, -13260, 250, 12860, 270)
    SetChrPos(0x000C, -12660, 250, 14050, 270)
    SetChrPos(0x000D, 15093, 250, 5901, 90)
    SetChrPos(0x000E, -12962, 0, 3438, 270)
    SetChrPos(0x000B, -370, 950, 12896, 0)
    CreateThread(0x000B, 0x00, 0x00, 0x000F)
    CreateThread(0x000D, 0x00, 0x00, 0x0002)
    FadeIn(1000, 0)
    OP_69(0x000D, 0)
    OP_0D()
    Sleep(1000)

    Fade(1000)
    OP_69(0x000B, 0)
    Sleep(1000)

    CreateThread(0x000E, 0x00, 0x00, 0x000E)
    Sleep(2900)

    Fade(1000)
    CameraMove(-9350, 250, 760, 0)
    Sleep(2800)

    SetChrDirection(0x000E, 225, 400)
    Sleep(500)

    TerminateThread(0x000E, 0xFF)
    OP_62(0x000E, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    Sleep(1000)

    Fade(1000)
    CameraMove(-18140, 250, 14540, 0)
    Sleep(1000)

    SetChrPos(0x000E, -12962, 0, 3438, 270)
    CreateThread(0x000E, 0x00, 0x00, 0x000E)
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010010712V#001F#3P哇～真的好壮观啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010713V#001F站得这么高，\n',
            '可以看到整个洛连特地区呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010714V#000F这么好的景色，\n',
            '说不定可以成为观光胜地哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020010715V#013F#3P嗯……也许吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(-15070, 250, 13930, 1000)
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(500)

    SetChrDirection(0x0101, 0, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010010716V#002F#3P………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010717V#002F怎么了？\n',
            '好像没什么精神啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000C, 225, 400)

    ChrTalk(
        0x000C,
        (
            '#0020010718V#019F#1P哈哈，真瞒不过你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010719V#019F来到塔顶之后……\n',
            '就一直感到有点不舒服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010720V#004F#3P没、没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020010721V#010F#1P嗯，稍微吹吹风，\n',
            '应该很快就会好起来的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010722V#010F反正机会难得，\n',
            '你就好好参观一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010723V#003F#3P可、可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020010724V#011F#1P借这样的机会扩展一下见识，\n',
            '也是作为游击士必要的工作态度啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010725V#011F如果看到什么有趣的事情，\n',
            '等一下也要告诉我哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010726V#007F#3P真是的，说不过你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010727V#000F我知道了，就稍微转转吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010728V#000F不过……\n',
            '如果觉得难受的话，要赶快叫我哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020010729V#019F#1P知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x000C, 0x0040)
    ClearChrFlags(0x000D, 0x0040)
    ClearChrFlags(0x000E, 0x0040)
    SetChrDirection(0x000C, 270, 400)
    CreateThread(0x000C, 0x00, 0x00, 0x0002)
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x39CE
@scena.Code('func_09_39CE')
def func_09_39CE():
    Sleep(1300)

    ChrWalkTo(0x0101, -256, 950, 13040, 3000, 0x00)

    Return()

# id: 0x000A offset: 0x39E8
@scena.Code('func_0A_39E8')
def func_0A_39E8():
    Sleep(2000)

    ChrWalkTo(0x000C, 1218, 0, 10022, 3000, 0x00)
    Sleep(1000)

    SetChrDirection(0x000C, 45, 400)

    Return()

# id: 0x000B offset: 0x3A0E
@scena.Code('func_0B_3A0E')
def func_0B_3A0E():
    Sleep(1500)

    ChrWalkTo(0x000D, -1084, 950, 12114, 3000, 0x00)

    Return()

# id: 0x000C offset: 0x3A28
@scena.Code('func_0C_3A28')
def func_0C_3A28():
    Sleep(1500)

    ChrWalkTo(0x000E, 225, 950, 11966, 3000, 0x00)

    Return()

# id: 0x000D offset: 0x3A42
@scena.Code('func_0D_3A42')
def func_0D_3A42():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3A7C',
    )

    ChrTurnDirection(0x0000, 0x00FE, 0)
    ChrTurnDirection(0x000C, 0x00FE, 0)
    ChrTurnDirection(0x000D, 0x00FE, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_3A71',
    )

    ChrTurnDirection(0x000E, 0x00FE, 0)

    Jump('loc_3A78')

    def _loc_3A71(): pass

    label('loc_3A71')

    ChrTurnDirection(0x000B, 0x00FE, 0)

    def _loc_3A78(): pass

    label('loc_3A78')

    Yield()

    Jump('func_0D_3A42')

    def _loc_3A7C(): pass

    label('loc_3A7C')

    Return()

# id: 0x000E offset: 0x3A7D
@scena.Code('func_0E_3A7D')
def func_0E_3A7D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3BB6',
    )

    SetChrChipByIndex(0x000E, 9)
    ChrWalkTo(0x000E, -12962, 0, 3438, 2000, 0x00)
    SetChrDirection(0x000E, 270, 400)
    SetChrChipByIndex(0x000E, 10)
    Sleep(2000)

    SetChrChipByIndex(0x000E, 9)
    ChrWalkTo(0x000E, -12210, 0, -3460, 2000, 0x00)
    SetChrDirection(0x000E, 225, 400)
    SetChrChipByIndex(0x000E, 10)
    Sleep(1500)

    SetChrChipByIndex(0x000E, 9)
    ChrWalkTo(0x000E, 51, 0, -503, 2000, 0x00)
    SetChrDirection(0x000E, 0, 400)
    SetChrDirection(0x000E, 180, 400)
    SetChrChipByIndex(0x000E, 10)
    Sleep(2000)

    SetChrChipByIndex(0x000E, 9)
    ChrWalkTo(0x000E, 7042, 0, 6382, 2000, 0x00)
    SetChrDirection(0x000E, 90, 400)
    SetChrChipByIndex(0x000E, 10)
    Sleep(1000)

    SetChrChipByIndex(0x000E, 9)
    ChrWalkTo(0x000E, 13070, 0, 13635, 2000, 0x00)
    SetChrDirection(0x000E, 45, 400)
    SetChrChipByIndex(0x000E, 10)
    Sleep(3000)

    SetChrChipByIndex(0x000E, 9)
    ChrWalkTo(0x000E, -23, 0, 8948, 2000, 0x00)
    SetChrDirection(0x000E, 0, 400)
    SetChrChipByIndex(0x000E, 10)
    Sleep(1000)

    SetChrChipByIndex(0x000E, 9)
    ChrWalkTo(0x000E, -5768, 0, 11523, 2000, 0x00)
    SetChrDirection(0x000E, 45, 400)
    SetChrChipByIndex(0x000E, 10)
    Sleep(2000)

    Jump('func_0E_3A7D')

    def _loc_3BB6(): pass

    label('loc_3BB6')

    Return()

# id: 0x000F offset: 0x3BB7
@scena.Code('func_0F_3BB7')
def func_0F_3BB7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3C52',
    )

    OP_97(0x000B, 142, 15900, 30000, 1000, 0x0001)
    ChrTurnDirectionByPos(0x000B, 142, 15900, 400)
    Sleep(1000)

    OP_97(0x000B, 142, 15900, -10000, 500, 0x0002)
    ChrTurnDirectionByPos(0x000B, 142, 15900, 400)
    Sleep(1000)

    OP_97(0x000B, 142, 15900, 5000, 700, 0x0002)
    Sleep(1000)

    OP_97(0x000B, 142, 15900, 50000, 1000, 0x0001)
    ChrTurnDirectionByPos(0x000B, 142, 15900, 400)
    Sleep(1000)

    Jump('func_0F_3BB7')

    def _loc_3C52(): pass

    label('loc_3C52')

    Return()

# id: 0x0010 offset: 0x3C53
@scena.Code('func_10_3C53')
def func_10_3C53():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 5, 0x255)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3CAD',
    )

    EventBegin(0x01)
    ClearMapFlags(0x00000001)

    ChrTalk(
        0x0101,
        (
            '#0010010730V#000F（……不能自己单独行动。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_3CAD(): pass

    label('loc_3CAD')

    Return()

# id: 0x0011 offset: 0x3CAE
@scena.Code('func_11_3CAE')
def func_11_3CAE():
    CreateThread(0x0008, 0x00, 0x00, 0x0012)
    CreateThread(0x0009, 0x00, 0x00, 0x0013)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    CameraMove(0, 1000, 12000, 4000)
    OP_A5(0x0001)
    OP_A5(0x0000)
    OP_20(0x000005DC)
    Sleep(1000)

    OP_21()

    ChrTalk(
        0x0008,
        (
            '#050F………………真奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#050F虽然感觉得到魔兽的气息，\n',
            '但是却看不见……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#070F#4S在上面，小心！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#050F什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayBGM(40)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000A, 0x0008)
    ClearChrFlags(0x000A, 0x0001)
    SetChrFlags(0x000A, 0x0004)
    SetChrPos(0x000A, 0, 10000, 16000, 0)

    ChrTalk(
        0x000A,
        (
            '#4S嘎呀呀呀呀呀啊啊啊！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    SetChrChipByIndex(0x000A, 5)
    ChrWalkTo(0x000A, 0, 1000, 11745, 6000, 0x00)
    CreateThread(0x000A, 0x03, 0x00, 0x0002)
    Sleep(500)

    SetChrChipByIndex(0x000A, 4)
    OP_A5(0x0001)
    OP_A5(0x0000)
    Sleep(1000)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    SetChrFlags(0x0008, 0x0008)
    SetChrFlags(0x0009, 0x0008)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0106, 0x0008)
    ClearChrFlags(0x0108, 0x0008)
    Battle(0x0000005E, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0008)
    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)
    OP_20(0x00000000)
    OP_21()
    Sleep(500)

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '辛苦了。\n',
            '战斗用体验版到此为止。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '本版本是为了测试战斗的感觉及\n',
            '手感而制作的版本，\n',
            '没有加入的要素还有很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '今后会根据各位测试员\n',
            '提交的意见和感想\n',
            '制作出更高完成度的体验版。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '──现在将返回主菜单。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    EventEnd(0x00)
    ClearMapFlags(0x00400000)
    NewScene('ED6_DT01/T0001._SN', 0, 0, 0)
    IdleLoop()
    SetMapFlags(0x00000001)

    Return()

# id: 0x0012 offset: 0x3F54
@scena.Code('func_12_3F54')
def func_12_3F54():
    OP_A6(0x0000)
    Sleep(500)

    ChrWalkTo(0x00FE, -100, 1000, 12313, 4000, 0x00)
    SetChrChipByIndex(0x00FE, 0)
    CreateThread(0x00FE, 0x03, 0x00, 0x0002)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A6(0x0000)
    Sleep(500)

    TerminateThread(0x00FE, 0x03)
    ChrTurnDirection(0x00FE, 0x000A, 0)
    ChrJumpToRelative(0x00FE, 0, 0, -4000, 2000, 7000)
    CreateThread(0x00FE, 0x03, 0x00, 0x0002)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Return()

# id: 0x0013 offset: 0x3FB4
@scena.Code('func_13_3FB4')
def func_13_3FB4():
    OP_A6(0x0001)
    Sleep(500)

    ChrWalkTo(0x00FE, 930, 0, 10461, 4000, 0x00)
    SetChrChipByIndex(0x00FE, 2)
    CreateThread(0x00FE, 0x03, 0x00, 0x0002)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A6(0x0001)
    Sleep(500)

    TerminateThread(0x00FE, 0x03)
    ChrTurnDirection(0x00FE, 0x000A, 0)
    ChrJumpToRelative(0x00FE, 1000, 0, -3000, 2000, 7000)
    CreateThread(0x00FE, 0x03, 0x00, 0x0002)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
