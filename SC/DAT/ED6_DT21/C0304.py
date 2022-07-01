import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0304_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0304   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '临时'),
    TXT(0x02, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0304.x'
    header.mapIndex       = 19
    header.bgm            = 125
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1582
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
    ]

# id: 0x10002 offset: 0xA8
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
    )

# id: 0x10003 offset: 0xC8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xC8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xC8
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 3480,
            triggerZ            = -170,
            triggerY            = 2770,
            triggerRange        = 1000,
            actorX              = 3450,
            actorZ              = 800,
            actorY              = 3430,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0xEC
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_106',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F0)
    Event(0, 0x0003)

    Jump('loc_129')

    def _loc_106(): pass

    label('loc_106')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_117',
    )

    OP_A3(0x10F1)
    Event(0, 0x0007)

    Jump('loc_129')

    def _loc_117(): pass

    label('loc_117')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 7, 0x1827)),
            Expr.Return,
        ),
        'loc_125',
    )

    Event(0, 0x0008)

    Jump('loc_129')

    def _loc_125(): pass

    label('loc_125')

    Event(0, 0x0004)

    def _loc_129(): pass

    label('loc_129')

    Return()

# id: 0x0001 offset: 0x12A
@scena.Code('Init')
def Init():
    SetMapFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0x00000000, 0x0000D6D8, 0x00000000)
    CreateThread(0x0008, 0x00, 0x00, 0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032D, 0, 0x1968)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_158',
    )

    OP_6F(0x0000, 0)

    Jump('loc_15F')

    def _loc_158(): pass

    label('loc_158')

    OP_6F(0x0000, 60)

    def _loc_15F(): pass

    label('loc_15F')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            (Expr.PushVar, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_185',
    )

    OP_65(0x00, 0x0001)
    OP_72(0x0000, 0x0000)
    OP_72(0x0000, 0x0004)

    Jump('loc_193')

    def _loc_185(): pass

    label('loc_185')

    OP_64(0x00, 0x0001)
    OP_71(0x0000, 0x0000)
    OP_71(0x0000, 0x0004)

    def _loc_193(): pass

    label('loc_193')

    Return()

# id: 0x0002 offset: 0x194
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0x08, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032D, 0, 0x1968)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_271',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['范围'], 1)"),
            Expr.Return,
        ),
        'loc_208',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['范围']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1968)

    Jump('loc_26E')

    def _loc_208(): pass

    label('loc_208')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['范围']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['范围']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)

    def _loc_26E(): pass

    label('loc_26E')

    Jump('loc_2A2')

    def _loc_271(): pass

    label('loc_271')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_2A2(): pass

    label('loc_2A2')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x2B0
@scena.Code('func_03_2B0')
def func_03_2B0():
    EventBegin(0x04)
    FadeOut(0, 16777215, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2DA',
    )

    Call(0, 0x0009)
    FadeIn(0, 0)
    Call(0, 0x000A)

    def _loc_2DA(): pass

    label('loc_2DA')

    SetChrPos(0x0101, 3980, -160, 2990, 0)
    SetChrPos(0x0103, 2730, -180, 2840, 0)
    SetChrPos(0x00F8, 4260, -180, 1570, 0)
    SetChrPos(0x00F9, 2840, -170, 1480, 0)
    OP_6D(3720, -160, 2770, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(3000, 16777215)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290842V#1007F#5P刚、刚才那是什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290843V#522F#6P铃声响起的同时、\n',
            '就被浓雾包围了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x0103, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030290844V#023F#5P这、这里是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010290845V#1004F#5P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    OP_1D(0x7D)
    OP_1F(0x50, 0x00000064)
    Sleep(300)

    OP_12(0x00000064, 0x000186A0, 0x00001388)

    @scena.Lambda('lambda_0473')
    def lambda_0473():
        OP_6B(6000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0473)

    Sleep(1000)

    @scena.Lambda('lambda_0488')
    def lambda_0488():
        OP_6C(135000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0488)

    OP_8C(0x0101, 90, 400)
    Sleep(100)

    OP_8C(0x00F8, 90, 400)
    Sleep(100)

    OP_8C(0x00F9, 180, 400)
    Sleep(500)

    OP_8C(0x0101, 0, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010290846V#1020F#5P！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290847V这，这……是哪里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_6D(3630, -150, 1970, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    OP_12(0x00000064, 0x0000D6D8, 0x00000000)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5A3',
    )

    ChrTalk(
        0x0107,
        (
            '#0070290848V#065F#5P不、不知不觉\n',
            '景色就变了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_62C')

    def _loc_5A3(): pass

    label('loc_5A3')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5E9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050290849V#552F#5P哼、不知不觉\n',
            '景色就变了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_62C')

    def _loc_5E9(): pass

    label('loc_5E9')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_62C',
    )

    ChrTalk(
        0x0105,
        (
            '#0060290850V#042F#5P……不知不觉\n',
            '景色就变了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_62C(): pass

    label('loc_62C')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_678',
    )

    ChrTalk(
        0x0108,
        (
            '#0080290851V#072F#5P难不成……\n',
            '是奇门遁甲之类的东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6BD')

    def _loc_678(): pass

    label('loc_678')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6BD',
    )

    ChrTalk(
        0x0104,
        (
            '#0040290852V#032F#5P唔，是被抛到\n',
            '别的地方了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6BD(): pass

    label('loc_6BD')

    OP_8C(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010290853V#1020F#5P雪拉姐……\n',
            '怎、怎么办？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_06FC')
    def lambda_06FC():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_06FC)

    Sleep(100)

    @scena.Lambda('lambda_070F')
    def lambda_070F():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_070F)

    Sleep(100)

    OP_8C(0x0103, 90, 400)

    ChrTalk(
        0x0103,
        (
            '#0030290854V#026F#6P镇定下来，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290855V#022F如果这是敌人做的手脚……\n',
            '必定会有逃脱的方法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290856V先试着找找看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270082V#1002F#5P嗯，嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CE(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CE(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CE(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x1825)
    OP_28(0x0092, 0x01, 0x0004)
    EventEnd(0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x7D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0004 offset: 0x80D
@scena.Code('func_04_80D')
def func_04_80D():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000068, 'loc_825'),
        (0x00000069, 'loc_84F'),
        (0x0000006B, 'loc_879'),
        (0x0000006A, 'loc_8A3'),
        (-1, 'loc_8CD'),
    )

    def _loc_825(): pass

    label('loc_825')

    OP_CE(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    OP_CE(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushVar, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_84C',
    )

    OP_CE(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_84C(): pass

    label('loc_84C')

    Jump('loc_8CD')

    def _loc_84F(): pass

    label('loc_84F')

    OP_CE(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    OP_CE(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushVar, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_876',
    )

    OP_CE(
        0x01,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_876(): pass

    label('loc_876')

    Jump('loc_8CD')

    def _loc_879(): pass

    label('loc_879')

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    OP_CE(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_8A0',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_8A0(): pass

    label('loc_8A0')

    Jump('loc_8CD')

    def _loc_8A3(): pass

    label('loc_8A3')

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    OP_CE(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_8CA',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_8CA(): pass

    label('loc_8CA')

    Jump('loc_8CD')

    def _loc_8CD(): pass

    label('loc_8CD')

    If(
        (
            (Expr.PushVar, 0x2),
            (Expr.PushLong, 0x14),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_8E3',
    )

    OP_A2(0x1842)
    Call(0, 0x0006)

    Jump('loc_9F1')

    def _loc_8E3(): pass

    label('loc_8E3')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_8FF',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            (Expr.PushVar, 0x0),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_90C')

    def _loc_8FF(): pass

    label('loc_8FF')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_90C(): pass

    label('loc_90C')

    If(
        (
            (Expr.PushVar, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_928',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x4),
            (Expr.PushVar, 0x1),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_935')

    def _loc_928(): pass

    label('loc_928')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushVar, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_935(): pass

    label('loc_935')

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushReg, 0x3),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_955',
    )

    Call(0, 0x0006)

    Jump('loc_9F1')

    def _loc_955(): pass

    label('loc_955')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 6, 0x1826)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_96E',
    )

    Call(0, 0x0005)

    Jump('loc_9F1')

    def _loc_96E(): pass

    label('loc_96E')

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Switch(
        (
            (Expr.PushReg, 0x4),
            Expr.Return,
        ),
        (0x00000000, 'loc_9A6'),
        (0x00000001, 'loc_9AE'),
        (0x00000002, 'loc_9B6'),
        (0x00000003, 'loc_9BE'),
        (0x00000004, 'loc_9C6'),
        (0x00000005, 'loc_9CE'),
        (0x00000006, 'loc_9D6'),
        (0x00000007, 'loc_9DE'),
        (0x00000008, 'loc_9E6'),
        (-1, 'loc_9EE'),
    )

    def _loc_9A6(): pass

    label('loc_9A6')

    OP_22(0x0118, 0x00, 0x64)

    Jump('loc_9EE')

    def _loc_9AE(): pass

    label('loc_9AE')

    OP_22(0x0118, 0x00, 0x5A)

    Jump('loc_9EE')

    def _loc_9B6(): pass

    label('loc_9B6')

    OP_22(0x0118, 0x00, 0x50)

    Jump('loc_9EE')

    def _loc_9BE(): pass

    label('loc_9BE')

    OP_22(0x0118, 0x00, 0x46)

    Jump('loc_9EE')

    def _loc_9C6(): pass

    label('loc_9C6')

    OP_22(0x0118, 0x00, 0x3C)

    Jump('loc_9EE')

    def _loc_9CE(): pass

    label('loc_9CE')

    OP_22(0x0118, 0x00, 0x32)

    Jump('loc_9EE')

    def _loc_9D6(): pass

    label('loc_9D6')

    OP_22(0x0118, 0x00, 0x28)

    Jump('loc_9EE')

    def _loc_9DE(): pass

    label('loc_9DE')

    OP_22(0x0118, 0x00, 0x1E)

    Jump('loc_9EE')

    def _loc_9E6(): pass

    label('loc_9E6')

    OP_22(0x0118, 0x00, 0x14)

    Jump('loc_9EE')

    def _loc_9EE(): pass

    label('loc_9EE')

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_9F1(): pass

    label('loc_9F1')

    Return()

# id: 0x0005 offset: 0x9F2
@scena.Code('func_05_9F2')
def func_05_9F2():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A12',
    )

    Call(0, 0x0009)
    FadeIn(0, 0)
    Call(0, 0x000A)

    def _loc_A12(): pass

    label('loc_A12')

    FadeOut(0, 0, -1)
    OP_0D()

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000068, 'loc_A35'),
        (0x00000069, 'loc_AB0'),
        (0x0000006B, 'loc_B2B'),
        (0x0000006A, 'loc_BA6'),
        (-1, 'loc_BA6'),
    )

    def _loc_A35(): pass

    label('loc_A35')

    SetChrPos(0x0101, -21430, 10, 3270, 0)
    SetChrPos(0x0103, -22780, -10, 3150, 0)
    SetChrPos(0x00F8, -21320, 0, 1950, 0)
    SetChrPos(0x00F9, -22600, 0, 1850, 0)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)

    Jump('loc_C21')

    def _loc_AB0(): pass

    label('loc_AB0')

    SetChrPos(0x0101, -22600, 0, 1850, 180)
    SetChrPos(0x0103, -21320, 0, 1950, 180)
    SetChrPos(0x00F8, -22780, -10, 3150, 180)
    SetChrPos(0x00F9, -21430, 10, 3270, 180)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)

    Jump('loc_C21')

    def _loc_B2B(): pass

    label('loc_B2B')

    SetChrPos(0x0101, -21430, 10, 3270, 90)
    SetChrPos(0x0103, -21320, 0, 1950, 90)
    SetChrPos(0x00F8, -22780, -10, 3150, 90)
    SetChrPos(0x00F9, -22600, 0, 1850, 90)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)

    Jump('loc_C21')

    def _loc_BA6(): pass

    label('loc_BA6')

    SetChrPos(0x0101, -22780, -10, 3150, 270)
    SetChrPos(0x0103, -22600, 0, 1850, 270)
    SetChrPos(0x00F8, -21430, 10, 3270, 270)
    SetChrPos(0x00F9, -21320, 0, 1950, 270)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)

    Jump('loc_C21')

    def _loc_C21(): pass

    label('loc_C21')

    FadeIn(1000, 0)
    OP_0D()
    OP_22(0x0118, 0x00, 0x50)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010290858V#1015F对了，雪拉姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290859V觉不觉得从刚才开始\n',
            '铃声就变大了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290860V#022F嗯嗯，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290861V说不定……\n',
            '线索就藏在铃声之中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1826)
    OP_28(0x0092, 0x01, 0x0008)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0xCFD
@scena.Code('func_06_CFD')
def func_06_CFD():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0308, 2, 0x1842)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D0C',
    )

    OP_2B(0x0092, 0x0003)

    def _loc_D0C(): pass

    label('loc_D0C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D2A',
    )

    Call(0, 0x0009)
    FadeIn(0, 0)
    Call(0, 0x000A)

    def _loc_D2A(): pass

    label('loc_D2A')

    FadeOut(0, 0, -1)
    OP_0D()

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000068, 'loc_D4D'),
        (0x00000069, 'loc_DC8'),
        (0x0000006B, 'loc_E43'),
        (0x0000006A, 'loc_EBE'),
        (-1, 'loc_EBE'),
    )

    def _loc_D4D(): pass

    label('loc_D4D')

    SetChrPos(0x0101, -21430, 10, 3270, 0)
    SetChrPos(0x0103, -22780, -10, 3150, 0)
    SetChrPos(0x00F8, -21320, 0, 1950, 0)
    SetChrPos(0x00F9, -22600, 0, 1850, 0)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)

    Jump('loc_F39')

    def _loc_DC8(): pass

    label('loc_DC8')

    SetChrPos(0x0101, -22600, 0, 1850, 180)
    SetChrPos(0x0103, -21320, 0, 1950, 180)
    SetChrPos(0x00F8, -22780, -10, 3150, 180)
    SetChrPos(0x00F9, -21430, 10, 3270, 180)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)

    Jump('loc_F39')

    def _loc_E43(): pass

    label('loc_E43')

    SetChrPos(0x0101, -21430, 10, 3270, 90)
    SetChrPos(0x0103, -21320, 0, 1950, 90)
    SetChrPos(0x00F8, -22780, -10, 3150, 90)
    SetChrPos(0x00F9, -22600, 0, 1850, 90)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)

    Jump('loc_F39')

    def _loc_EBE(): pass

    label('loc_EBE')

    SetChrPos(0x0101, -22780, -10, 3150, 270)
    SetChrPos(0x0103, -22600, 0, 1850, 270)
    SetChrPos(0x00F8, -21430, 10, 3270, 270)
    SetChrPos(0x00F9, -21320, 0, 1950, 270)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)

    Jump('loc_F39')

    def _loc_F39(): pass

    label('loc_F39')

    FadeIn(1000, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0308, 2, 0x1842)),
            Expr.Return,
        ),
        'loc_1197',
    )

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290862V#1007F从刚才开始就感觉\n',
            '一直在同一个地方绕……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290863V#1015F怎么办好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290864V#522F……是啊………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290865V#022F不过，可以肯定，\n',
            '线索一定就是铃声的大小。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290866V只要能抓住这个法则就一定……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_22(0x0118, 0x00, 0x64)
    OP_20(0x00000BB8)
    OP_12(0x00000064, 0x00002710, 0x00001770)
    Sleep(3000)

    ChrTalk(
        0x0101,
        (
            '#0010290867V#1020F又来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10B0',
    )

    ChrTalk(
        0x0107,
        (
            '#0070290840V#065F啊哇哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1167')

    def _loc_10B0(): pass

    label('loc_10B0')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10DE',
    )

    ChrTalk(
        0x0105,
        (
            '#0060290839V#043F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1167')

    def _loc_10DE(): pass

    label('loc_10DE')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_110C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040290838V#033F噢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1167')

    def _loc_110C(): pass

    label('loc_110C')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_113C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050290837V#057F可恶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1167')

    def _loc_113C(): pass

    label('loc_113C')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1167',
    )

    ChrTalk(
        0x0108,
        (
            '#0080290836V#072F呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1167(): pass

    label('loc_1167')

    ChrTalk(
        0x0103,
        (
            '#0030290873V#025F……似乎到时间了………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12EB')

    def _loc_1197(): pass

    label('loc_1197')

    OP_22(0x0118, 0x00, 0x64)
    OP_20(0x00000BB8)
    OP_12(0x00000064, 0x00002710, 0x00001770)
    Sleep(3000)

    ChrTalk(
        0x0101,
        (
            '#0010290874V#1005F又来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1207',
    )

    ChrTalk(
        0x0107,
        (
            '#0070290840V#065F啊哇哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12BE')

    def _loc_1207(): pass

    label('loc_1207')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1235',
    )

    ChrTalk(
        0x0105,
        (
            '#0060290839V#043F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12BE')

    def _loc_1235(): pass

    label('loc_1235')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1263',
    )

    ChrTalk(
        0x0104,
        (
            '#0040290838V#033F噢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12BE')

    def _loc_1263(): pass

    label('loc_1263')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1293',
    )

    ChrTalk(
        0x0106,
        (
            '#0050290837V#057F可恶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12BE')

    def _loc_1293(): pass

    label('loc_1293')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12BE',
    )

    ChrTalk(
        0x0108,
        (
            '#0080290836V#072F呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12BE(): pass

    label('loc_12BE')

    ChrTalk(
        0x0103,
        (
            '#0030290880V#022F……似乎走出来了………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_12EB(): pass

    label('loc_12EB')

    OP_12(0x00000064, 0x00002710, 0x000007D0)
    Sleep(2000)

    OP_A2(0x10F0)
    NewScene('ED6_DT21/C0303._SN', 100, 20, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x130A
@scena.Code('func_07_130A')
def func_07_130A():
    EventBegin(0x00)
    SetChrPos(0x0101, 8300, 0, 5920, 0)
    OP_6D(8300, 0, 5920, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(148000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010290884V#1000F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 400)
    Sleep(500)

    OP_8C(0x0101, 0, 400)
    OP_8C(0x0101, 270, 400)
    Sleep(500)

    OP_8C(0x0101, 180, 400)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010290885V#1000F这，是哪里……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290886V雪拉姐，大家……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290887V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x1828)
    OP_28(0x0092, 0x01, 0x0020)
    OP_28(0x0092, 0x01, 0x0040)
    OP_28(0x0092, 0x01, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x143A
@scena.Code('func_08_143A')
def func_08_143A():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_144F',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_144F(): pass

    label('loc_144F')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1474',
    )

    EventBegin(0x00)
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene('ED6_DT21/T0300._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1474(): pass

    label('loc_1474')

    Return()

# id: 0x0009 offset: 0x1475
@scena.Code('func_09_1475')
def func_09_1475():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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
        (0x00000000, 'loc_14F2'),
        (0x00000001, 'loc_14F8'),
        (-1, 'loc_14FE'),
    )

    def _loc_14F2(): pass

    label('loc_14F2')

    OP_A2(0x1200)

    Jump('loc_14FE')

    def _loc_14F8(): pass

    label('loc_14F8')

    OP_A2(0x1201)

    Jump('loc_14FE')

    def _loc_14FE(): pass

    label('loc_14FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_150C',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_1510')

    def _loc_150C(): pass

    label('loc_150C')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_1510(): pass

    label('loc_1510')

    Return()

# id: 0x000A offset: 0x1511
@scena.Code('func_0A_1511')
def func_0A_1511():
    ClearMapFlags(0x00000001)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0002,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0003,
            0x0004,
            0x0006,
            0x0007,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)
    Sleep(1000)

    Return()

# id: 0x000B offset: 0x1563
@scena.Code('func_0B_1563')
def func_0B_1563():
    OP_1F(0x50, 0x000000C8)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
