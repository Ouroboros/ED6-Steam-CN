import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R1504_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1504   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '特务兵'),
    TXT(0x02, '特务兵'),
    TXT(0x03, '特务兵'),
    TXT(0x04, '拉文努山道方向'),
    TXT(0x05, '拉文努山道方向'),
    TXT(0x06, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'R1504.x'
    header.mapIndex       = 59
    header.bgm            = 31
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xB1A
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
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT27/CH03095._CH', 'ED6_DT27/CH03095P._CP'),
        ('ED6_DT07/CH00055._CH', 'ED6_DT07/CH00055P._CP'),
        ('ED6_DT07/CH00025._CH', 'ED6_DT07/CH00025P._CP'),
    ]

# id: 0x10002 offset: 0xCA
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -111060,
            z                   = -20,
            y                   = -19200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 1140,
            z                   = 10,
            y                   = -19200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x16A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x16A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x16A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x16A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_17D',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0002)

    def _loc_17D(): pass

    label('loc_17D')

    Return()

# id: 0x0001 offset: 0x17E
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_192'),
        (0x00000065, 'loc_1AC'),
        (0x00000066, 'loc_1AC'),
        (-1, 'loc_1C6'),
    )

    def _loc_192(): pass

    label('loc_192')

    OP_16(0x02, 0x00000FA0, 0xFFFE0FE8, 0xFFFE2758, 0x0023006B)
    ClearChrFlags(0x000B, 0x0004)

    Jump('loc_1C6')

    def _loc_1AC(): pass

    label('loc_1AC')

    OP_16(0x02, 0x00000FA0, 0xFFFC5A68, 0xFFFE2758, 0x00230022)
    ClearChrFlags(0x000C, 0x0004)

    Jump('loc_1C6')

    def _loc_1C6(): pass

    label('loc_1C6')

    Return()

# id: 0x0002 offset: 0x1C7
@scena.Code('ReInit')
def ReInit():
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
        'loc_1DA',
    )

    Call(0, 0x0003)

    def _loc_1DA(): pass

    label('loc_1DA')

    FormationDelMember(0x00, 0xFF)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1EE',
    )

    FormationDelMember(0x05, 0xFF)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF6, 0xFF)

    Jump('loc_1F5')

    def _loc_1EE(): pass

    label('loc_1EE')

    FormationDelMember(0x02, 0xFF)
    FormationAddMember(ChrTable['阿加特'], 0xF6, 0xFF)

    def _loc_1F5(): pass

    label('loc_1F5')

    FormationAddMember(ChrTable['亚妮拉丝'], 0xF7, 0xFF)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0008, 2290, 0, 12140, 0)
    SetChrPos(0x0009, 1210, 0, 11140, 0)
    SetChrPos(0x000A, 2840, 0, 10990, 0)
    OP_6D(2290, 0, 12140, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_6A(0x0008)
    OP_C8(0x0200, 0x0046, 'C_PLAC16._CH', 0x00, 0x07D0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_029F')
    def lambda_029F():
        OP_8E(0x00FE, 2290, 0, 22140, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_029F)

    Sleep(100)

    @scena.Lambda('lambda_02BF')
    def lambda_02BF():
        OP_8E(0x00FE, 1210, 0, 21140, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_02BF)

    Sleep(50)

    @scena.Lambda('lambda_02DF')
    def lambda_02DF():
        OP_8E(0x00FE, 2840, 0, 20990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_02DF)

    WaitForThreadExit(0x000A, 0x0001)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_22(0x006E, 0x00, 0x64)
    ClearMapFlags(0x00000001)
    OP_6D(-110000, 0, 21330, 0)
    SetChrPos(0x0008, -110000, 0, 21330, 0)
    SetChrPos(0x0009, -110700, 0, 20190, 0)
    SetChrPos(0x000A, -109100, 0, 20200, 0)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    @scena.Lambda('lambda_036C')
    def lambda_036C():
        OP_8E(0x00FE, -110000, 0, 28310, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_036C)

    Sleep(300)

    @scena.Lambda('lambda_038C')
    def lambda_038C():
        OP_8E(0x00FE, -110000, 0, 28310, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_038C)

    Sleep(300)

    @scena.Lambda('lambda_03AC')
    def lambda_03AC():
        OP_8E(0x00FE, -110000, 0, 26310, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_03AC)

    WaitForThreadExit(0x000A, 0x0001)
    Sleep(1000)

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    Fade(1000)
    SetChrPos(0x00F6, -104360, -70, 7570, 0)
    SetChrPos(0x010A, -103210, -50, 6530, 0)
    SetChrFlags(0x00F6, 0x0002)
    SetChrFlags(0x010A, 0x0002)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_41A',
    )

    SetChrChipByIndex(0x00F6, 2)

    Jump('loc_41F')

    def _loc_41A(): pass

    label('loc_41A')

    SetChrChipByIndex(0x00F6, 3)

    def _loc_41F(): pass

    label('loc_41F')

    SetChrSubChip(0x00F6, 1)
    SetChrChipByIndex(0x010A, 1)
    SetChrSubChip(0x010A, 1)
    OP_6D(-103630, -60, 7990, 0)
    OP_6E(239, 0)
    OP_0D()
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_6C0',
    )

    ChrTalk(
        0x010A,
        (
            '#0120260001V#816F呵呵……\n',
            '看来是猜对了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260002V#051F啊啊……\n',
            '总算抓住狐狸尾巴啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260003V不过真没想到\n',
            '竟然会是拉文努废坑啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260004V这些家伙\n',
            '倒是挺会选地点的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260005V#818F记得是空贼团\n',
            '抢夺定期船货物\n',
            '所利用过的地方吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260006V#053F好像是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260007V#050F艾丝蒂尔他们\n',
            '似乎在途中的露天采掘场\n',
            '和空贼团的人交战过吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260008V#817F这么说来……\n',
            '把这里做为大本营\n',
            '的可能性似乎很高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260009V#812F如何？\n',
            '就这样闯进去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260010V#057F啊啊，没空跟\n',
            '协会和军方联络了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260011V总之先潜入进去\n',
            '确认余党的规模吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260012V#816F明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_91B')

    def _loc_6C0(): pass

    label('loc_6C0')

    ChrTalk(
        0x010A,
        (
            '#0120260001V#816F呵呵……\n',
            '看来是猜对了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260014V#026F嗯……\n',
            '总算抓住狐狸尾巴了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260015V#027F不过真没想到\n',
            '竟然是拉文努废坑呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260016V这些家伙\n',
            '倒是挺会选地点的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260017V#818F记得是空贼团\n',
            '抢夺定期船货物\n',
            '所利用过的地方吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260018V#020F嗯嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260019V我们在途中的露天采掘场\n',
            '和空贼团的那些人交战过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260008V#817F这么说来……\n',
            '把这里做为大本营\n',
            '的可能性似乎很高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120260009V#812F如何？\n',
            '就这样闯进去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260022V#022F嗯嗯，没空跟\n',
            '协会和军方联络了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260023V总之先潜入进去\n',
            '确认余党的规模吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120260012V#816F明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_91B(): pass

    label('loc_91B')

    OP_DB()
    Sleep(200)

    Fade(1000)
    SetChrPos(0x00F6, -113220, 20, 9490, 0)
    SetChrPos(0x010A, -107140, 40, 9700, 0)
    OP_6D(-110000, 0, 21330, 0)
    OP_6E(262, 0)
    OP_0D()
    ClearChrFlags(0x00F6, 0x0002)
    ClearChrFlags(0x010A, 0x0002)
    SetChrChipByIndex(0x00F6, 65535)
    SetChrChipByIndex(0x010A, 65535)
    SetChrFlags(0x010A, 0x0004)

    @scena.Lambda('lambda_0982')
    def lambda_0982():
        OP_8E(0x00FE, -111950, 100, 22290, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F6, 0x0001, lambda_0982)

    Sleep(500)

    @scena.Lambda('lambda_09A2')
    def lambda_09A2():
        OP_8E(0x00FE, -107700, 80, 22290, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_09A2)

    WaitForThreadExit(0x00F6, 0x0001)
    OP_8C(0x00F6, 180, 800)
    WaitForThreadExit(0x010A, 0x0001)
    OP_8C(0x010A, 180, 800)
    Sleep(1000)

    ChrTurnDirection(0x00F6, 0x010A, 400)
    Sleep(500)

    OP_8C(0x010A, 270, 400)
    Sleep(1000)

    OP_8E(0x00F6, -110810, -10, 22080, 5000, 0x00)

    @scena.Lambda('lambda_0A06')
    def lambda_0A06():
        OP_8E(0x00FE, -108850, -20, 22030, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_0A06)

    @scena.Lambda('lambda_0A21')
    def lambda_0A21():
        OP_8E(0x00FE, -110000, 0, 28310, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F6, 0x0001, lambda_0A21)

    WaitForThreadExit(0x010A, 0x0001)
    ClearChrFlags(0x010A, 0x0004)

    @scena.Lambda('lambda_0A46')
    def lambda_0A46():
        OP_8E(0x00FE, -110000, 0, 28310, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_0A46)

    Sleep(300)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C1104._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0xA79
@scena.Code('func_03_A79')
def func_03_A79():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
        (0x00000000, 'loc_AF3'),
        (0x00000001, 'loc_AF9'),
        (-1, 'loc_AFF'),
    )

    def _loc_AF3(): pass

    label('loc_AF3')

    OP_A2(0x1200)

    Jump('loc_AFF')

    def _loc_AF9(): pass

    label('loc_AF9')

    OP_A2(0x1201)

    Jump('loc_AFF')

    def _loc_AFF(): pass

    label('loc_AFF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_B0D',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_B11')

    def _loc_B0D(): pass

    label('loc_B0D')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_B11(): pass

    label('loc_B11')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
