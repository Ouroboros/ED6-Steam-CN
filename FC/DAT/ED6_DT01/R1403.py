import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R1403_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1403   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '吉尔'),
    TXT(0x02, '乔丝特'),
    TXT(0x03, '空贼阿伦'),
    TXT(0x04, '空贼雷古'),
    TXT(0x05, '空贼蒂诺'),
    TXT(0x06, '空贼莱尔'),
    TXT(0x07, '空贼洛西'),
    TXT(0x08, '空贼罗尔'),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'R1403.x'
    header.mapIndex       = 58
    header.bgm            = 86
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x11D6
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
            word_3A         = 58,
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
        ('ED6_DT07/CH02120._CH', 'ED6_DT07/CH02120P._CP'),
        ('ED6_DT07/CH02130._CH', 'ED6_DT07/CH02130P._CP'),
        ('ED6_DT07/CH01380._CH', 'ED6_DT07/CH01380P._CP'),
    ]

# id: 0x10002 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 26500,
            z                   = 0,
            y                   = 12600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0141,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 26500,
            z                   = 0,
            y                   = 12600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0141,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 800,
            z                   = 500,
            y                   = 500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -500,
            z                   = 500,
            y                   = 900,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -3200,
            z                   = 500,
            y                   = -700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -2300,
            z                   = 500,
            y                   = -2700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -1000,
            z                   = 500,
            y                   = -2800,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 1000,
            z                   = 500,
            y                   = -1900,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1C2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1C2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1C2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1C2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_1DE',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    SetMapFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x57),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0004)

    def _loc_1DE(): pass

    label('loc_1DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_1EC',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0003)

    def _loc_1EC(): pass

    label('loc_1EC')

    Return()

# id: 0x0001 offset: 0x1ED
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -128000, -128000, 196638)

    Return()

# id: 0x0002 offset: 0x200
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_215',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_215(): pass

    label('loc_215')

    Return()

# id: 0x0003 offset: 0x216
@scena.Code('func_03_216')
def func_03_216():
    FormationAddMember(0x03, 0xFF)
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(12760, -10, 9570, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(4600, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 100)
    SetChrPos(0x0101, 6340, -210, -12440, 315)
    SetChrPos(0x0102, 7380, -380, -12200, 315)
    SetChrPos(0x0103, 5970, -290, -13400, 315)
    SetChrPos(0x0104, 12230, 1020, -21130, 319)
    ChrTurnDirectionByPos(0x000A, -1100, -720, 0)
    ChrTurnDirectionByPos(0x000B, -1100, -720, 0)
    ChrTurnDirectionByPos(0x000C, -1100, -720, 0)
    ChrTurnDirectionByPos(0x000D, -1100, -720, 0)
    ChrTurnDirectionByPos(0x000E, -1100, -720, 0)
    ChrTurnDirectionByPos(0x000F, -1100, -720, 0)
    FadeIn(2000, 0)
    CameraMove(1960, -10, 2560, 5000)
    Fade(1000)
    CameraMove(3800, 120, -9560, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0103,
        (
            '#0030031290V#020F#6P原来停在了『琥珀之塔』前面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031291V这里的确是\n',
            '街道外面最好的停降场所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x000F, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_485',
    )

    ChrTalk(
        0x0101,
        (
            '#0010031292V#002F#5P『琥珀之塔』？\n',
            '是和洛连特的『翡翠之塔』\n',
            '一样的塔吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031293V#012F#2P嗯，它们同样都是\n',
            '被称为『四轮之塔』的古代遗迹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031294V那么雪拉姐姐……\n',
            '我们要马上将他们制服吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C3')

    def _loc_485(): pass

    label('loc_485')

    ChrTalk(
        0x0102,
        (
            '#0020031295V#012F#2P那么雪拉姐姐……\n',
            '我们要马上将他们制服吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C3(): pass

    label('loc_4C3')

    ChrTalk(
        0x0103,
        (
            '#0030031296V#522F#6P这个嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031297V和之前交手时相比，\n',
            '他们的人手增加了好几倍……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031298V#006F#5P没关系啦。\n',
            '反正也还没到无法对付的数量。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031299V只要我们一口气解决的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0104,
        '青年的声音',
        (
            '#0040031300V#1P呵呵……\n',
            '我想还是不要这样比较好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_05BB')
    def lambda_05BB():
        CameraMove(6810, -410, -12820, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_05BB)

    @scena.Lambda('lambda_05D3')
    def lambda_05D3():
        ChrTurnDirection(0x00FE, 0x0104, 400)
        Yield()

        Jump('lambda_05D3')

    DispatchAsync2(0x0101, 0x0001, lambda_05D3)

    @scena.Lambda('lambda_05E4')
    def lambda_05E4():
        ChrTurnDirection(0x00FE, 0x0104, 400)
        Yield()

        Jump('lambda_05E4')

    DispatchAsync2(0x0102, 0x0001, lambda_05E4)

    @scena.Lambda('lambda_05F5')
    def lambda_05F5():
        ChrTurnDirection(0x00FE, 0x0104, 400)
        Yield()

        Jump('lambda_05F5')

    DispatchAsync2(0x0103, 0x0001, lambda_05F5)

    SetChrFlags(0x0104, 0x0004)
    ChrWalkTo(0x0104, 10320, 920, -18960, 5000, 0x00)
    ChrJumpTo(0x0104, 9190, -110, -16280, 1000, 5000)
    ClearChrFlags(0x0104, 0x0004)
    ChrWalkTo(0x0104, 7460, -500, -14130, 5000, 0x00)
    SetChrDirection(0x0104, 315, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#0040031301V#031F呀，让大家久等了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031302V#004F#3S#5P奥、奥利维',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0103, 0x01)

    ChrTalk(
        0x0102,
        (
            '#0020031303V#012F小声一点……\n',
            '会被他们发现的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031304V#002F#5P………（紧张紧张）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)
    ChrTurnDirection(0x0102, 0x0104, 0)

    ChrTalk(
        0x0103,
        (
            '#0030031305V#023F真让人吃惊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031306V想不到你能这么快\n',
            '从那种醉死的状态恢复过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0103, 400)

    ChrTalk(
        0x0104,
        (
            '#0040031307V#035F呵呵，小菜一碟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031308V我只不过把胃里的东西都吐光，\n',
            '顺便用冷水淋头罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010031309V#007F#5P难、难以置信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031310V#018F或者说是可怕的执著……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031311V#031F如此有趣的事情，\n',
            '本人怎么能错过呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031312V离开旅馆的时候，\n',
            '正好看到你们向街道外面跑出去，\n',
            '所以我就紧跟着过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031313V#025F我还是太大意了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031314V一下子用上那么多烈酒，\n',
            '竟然还是没能把你灌醉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x0104,
        (
            '#0040031315V#034F刚刚确实是差点要了我的小命啊，\n',
            '雪拉君你还是饶了我吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031316V#030F话说回来，你们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031317V你们难道不觉得\n',
            '在这里和空贼战斗很无聊吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031318V#009F#5P什么无聊！我们又不是来玩的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031319V#032F等一下，我可是认真的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031320V在这里战斗的话，\n',
            '就算抓到那对兄妹好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031321V接下来要是无法保证\n',
            '能从他们口中问出空贼的据点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031322V到那时候，可能连释放人质\n',
            '之类的要求也都变得难以实现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031323V#022F任何事都要带点风险吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031324V难道说，\n',
            '你有不冒风险的好办法吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031325V#031F呵·呵·呵……\n',
            '各位，把耳朵凑过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031326V#509F#5P好吧，不过我事先声明……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031327V如果你敢在我耳边吹气，\n',
            '我真的会揍你哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(1000)

    SetChrPos(0x0008, -340, -40, -16430, 0)
    SetChrPos(0x0009, 700, -10, -16580, 0)
    CameraMove(-1120, 520, -1770, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3730, 0)
    OP_6C(224000, 0)
    OP_6E(261, 0)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(1000)

    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x000E, 255)
    OP_4A(0x000F, 255)
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000E, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000F, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_0D25')
    def lambda_0D25():
        ChrWalkTo(0x00FE, -1370, 270, -5070, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0D25)

    @scena.Lambda('lambda_0D40')
    def lambda_0D40():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0D40')

    DispatchAsync2(0x000A, 0x0001, lambda_0D40)

    @scena.Lambda('lambda_0D51')
    def lambda_0D51():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0D51')

    DispatchAsync2(0x000B, 0x0001, lambda_0D51)

    @scena.Lambda('lambda_0D62')
    def lambda_0D62():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0D62')

    DispatchAsync2(0x000C, 0x0001, lambda_0D62)

    @scena.Lambda('lambda_0D73')
    def lambda_0D73():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0D73')

    DispatchAsync2(0x000D, 0x0001, lambda_0D73)

    @scena.Lambda('lambda_0D84')
    def lambda_0D84():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0D84')

    DispatchAsync2(0x000E, 0x0001, lambda_0D84)

    @scena.Lambda('lambda_0D95')
    def lambda_0D95():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0D95')

    DispatchAsync2(0x000F, 0x0001, lambda_0D95)

    Sleep(800)

    @scena.Lambda('lambda_0DAB')
    def lambda_0DAB():
        ChrWalkTo(0x00FE, -500, 150, -5770, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0DAB)

    CameraMove(-1870, 520, -4370, 3000)

    ChrTalk(
        0x000A,
        (
            '#1250031328V吉尔大哥，大小姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1040031329V欢迎回来！\n',
            '我们等了很久呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1050031330V谈话的内容很多吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0290031331V#200F#5P啊啊……\n',
            '终于要上演压轴戏了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031332V包括王国军的动向，\n',
            '这次我们得到了很多情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0990031333V那么，终于……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0090031334V#210F#5P嗯，\n',
            '最近几天应该就可以拿到赎金了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090031335V可以说，\n',
            '现在正朝我们的梦想一步步迈进呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000E, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000F, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '#1260031336V呀嗬——！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#1270031337V太棒了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0290031338V#200F#5P喂喂，\n',
            '现在高兴还太早了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031339V总之先回据点\n',
            '向多伦大哥报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0090031340V#211F#5P大家，快点撤退吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1250031341V#5A#3P#1K收到！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000B,
        (
            '#5A#4P#1K收到！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000C,
        (
            '#5A#2P#1K收到！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000D,
        (
            '#5A#2P#1K收到！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000E,
        (
            '#5A#1P#1K收到！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000F,
        (
            '#5A#3P#1K收到！',
            TxtCtl.Enter,
        ),
    )

    OP_56(0x01)
    OP_59()
    OP_20(0x000005DC)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Sleep(1000)

    NewScene('ED6_DT01/E0110._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x10E0
@scena.Code('func_04_10E0')
def func_04_10E0():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    CameraMove(16867, 6300, -3100, 0)
    CameraSetDistance(4400, 0)
    OP_67(0, 2500, -10000, 0)
    OP_6C(324000, 0)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 10000)

    @scena.Lambda('lambda_1157')
    def lambda_1157():
        CameraMove(14820, 6300, -3700, 15000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1157)

    @scena.Lambda('lambda_116F')
    def lambda_116F():
        CameraSetDistance(5500, 15000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_116F)

    @scena.Lambda('lambda_117F')
    def lambda_117F():
        OP_6C(135000, 15000)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_117F)

    @scena.Lambda('lambda_118F')
    def lambda_118F():
        OP_67(0, 10600, -10000, 15000)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_118F)

    PlaySE(121, 0x00, 0x64)
    Sleep(6500)

    PlaySE(205, 0x00, 0x64)
    Sleep(8500)

    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    SetMapFlags(0x02000000)
    ClearMapFlags(0x10000000)
    NewScene('ED6_DT01/E0110._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
